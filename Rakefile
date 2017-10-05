require 'open3'

task :test do
  Open3.popen3(File.expand_path('server')) do |i, o, e, wt|
    `python3 tests.py`
    Process.kill('KILL', wt.pid)
  end
end
