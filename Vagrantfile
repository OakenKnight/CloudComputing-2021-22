Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"
  config.vm.provision :docker 
  # config.vm.provision :docker_compose
  config.vm.provision "shell", path:"script.sh"

  config.vm.provision "file", source: "./cloud_computing_project", destination: "cloud_computing_project"

end