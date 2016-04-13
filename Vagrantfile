# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version "< 1.7"
Vagrant.require_version ">= 1.6"

Vagrant.configure("2") do |config|
  config.vm.define :default do |host|
    host.vm.box = "debian/jessie64"
    host.vm.box_check_update = true
    host.vm.network "private_network", ip: "192.168.255.254"
    host.vm.network "forwarded_port", guest: 5000, host: 5000
    host.vm.provision "shell", path: "provision_local.sh"
    host.vm.synced_folder ".", "/vagrant"
  end
end
