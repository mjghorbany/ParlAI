# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import parlai.tasks.wikimovies.build as wikimovies_build
import os


def build(opt):
    # Depends upon another dataset, wikimovies, build that first.
    wikimovies_build.build(opt)

    dpath = os.path.join(opt['datapath'], 'DBLL')
    if not build_data.built(dpath):
        print('[building data: ' + dpath + ']')
        build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        fname = 'dbll.tgz'
        url = 'https://s3.amazonaws.com/fair-data/parlai/dbll/' + fname
        build_data.download(url, dpath, fname)
        build_data.untar(dpath, fname)

        # Mark the data as built.
        build_data.mark_done(dpath)
