require 'open3'

task :test do
  Open3.popen3('./server') do |i, o, e, wt|
    `python3 server_test.py`
    Process.kill('KILL', wt.pid)
  end
end