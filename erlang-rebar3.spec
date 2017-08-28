%global realname rebar3
%global upstream rebar3
%global debug_package %{nil}

# Set this to true when starting a rebuild of the whole erlang stack. There's
# a cyclical dependency between erlang-rebar and erlang-getopt so this package
# (rebar) needs to get built first in bootstrap mode.


Name:		erlang-%{realname}
Version:	3.4.2
Release:	%mkrel 1
Summary:	Erlang Build Tools
Group:		Development/Tools
License:	MIT
URL:		http://www.rebar3.org
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
#Source1:	rebar.escript

BuildRequires:	erlang-asn1
BuildRequires:	erlang-common_test
BuildRequires:	erlang-compiler
BuildRequires:	erlang-crypto
BuildRequires:	erlang-dialyzer
BuildRequires:	erlang-diameter
BuildRequires:	erlang-edoc
BuildRequires:	erlang-erl_interface
BuildRequires:	erlang-eunit
BuildRequires:	erlang-parsetools
BuildRequires:	erlang-reltool
BuildRequires:	erlang-snmp
BuildRequires:	erlang-syntax_tools
BuildRequires:	erlang-tools
BuildRequires:  erlang-public_key


# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-common_test%{?_isa}
# Requires for port compiling - no direct references in Rebar's src/*.erl files
Requires:	erlang-erl_interface%{?_isa}
# This one cannot be picked up automatically
# See https://bugzilla.redhat.com/960079
Requires:	erlang-parsetools%{?_isa}

#Requires:	erlang-rpm-macros >= 0.2.2
Provides:	%{realname} = %{version}-%{release}


%description
Erlang Build Tools.


%prep
%setup -q -n %{realname}-%{version}

%build
./bootstrap
./rebar3 compile -v


%install
# Install rebar script itself
install -D -p -m 0755 rebar3 %{buildroot}%{_bindir}/rebar3
# Copy the contents of priv folder
#cp -a priv %{buildroot}%{_libdir}/erlang/%{realname}-%{version}/


%check


%files
%doc README.md THANKS rebar.config.sample
#%license LICENSE
%{_bindir}/rebar3
#%{erlang_appdir}/




%changelog
* Thu Nov 17 2016 neoclust <neoclust> 2.6.4-1.mga6
+ Revision: 1067928
- new version 2.6.4

  + pterjan <pterjan>
    - Disable bootstrap

* Thu Jun 16 2016 tv <tv> 2.6.1-12.mga6
+ Revision: 1021689
- arm bootstrap

* Fri May 06 2016 neoclust <neoclust> 2.6.1-11.mga6
+ Revision: 1009775
- Rebuild post boostrap
- imported package erlang-rebar

