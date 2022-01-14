Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"
  # config.vm.provision :docker_compose
  # config.vm.provision "shell", path:"script.sh"

  config.vm.provision "file", source: "./cloud_computing_project", destination: "cloud_computing_project"
  config.vm.provision "file", source: "./nginx", destination: "nginx"
  config.vm.provision "file", source: "poetry.lock", destination: "poetry.lock"
  config.vm.provision "file", source: "pyproject.toml", destination: "pyproject.toml"
  config.vm.provision "file", source: "Dockerfile", destination: "Dockerfile"

  config.vm.provision "file", source: "docker-compose.yml", destination: "docker-compose.yml"

  config.vm.provision :docker 
  config.vm.provision :shell, path: "./install-compose.sh"
  config.vm.provision :shell, path: "./docker-compose-up.sh"

  config.vm.network "forwarded_port", guest: 8080, host: 5000, host_ip: "127.0.0.1"

end