# we have the times of each cyclist and stage
# for the participants in the last local
# cycle tour. The cyclists lists contains a
# series of names. The matrix has a row for
# each cyclist, in the same order that they
# appear in cyclists. Each row has the time
# in secods (a floating value) invested
# in each of the 5 stages of the race.
#
# is requested:
#
# a function that receives the list and the
# matrix and returns the winner of the round,
# the one whose sum of times in the stages
# is minimal
#
# a function that receives the list and array
# and a stage number and returns the name
# of the stage winner
#
# a prcedure that receives the list
# and the matrix and shows the winner of each
# stage on the screen.

import numpy as np


def winner(lcyclist, ltimes):
    mini = np.min(ltimes)
    if mini in ltimes[0:]:
        return(lcyclist[0])
    if mini in ltimes[1:]:
        return(lcyclist[1])
    if mini in ltimes[2:]:
        return(lcyclist[2])


def stageWinner(lcyclist, ltimes, stage):

    stage = stage - 1

    if stage <= ltimes.shape[1]:
        columStage = np.array(ltimes[:, stage], dtype=float)
        stageWin = np.min(ltimes[:, stage])

        for i, o in enumerate(columStage):
            if columStage[i] == stageWin:
                return lcyclist[i]


def winnerEcahStage(lcyclists, ltimes):

    for i in range(0, (ltimes.shape[1])):

        winner = np.min(ltimes[:, i])

        for j, o in enumerate(lcyclists):

            timeStage = np.array(ltimes[j, :], dtype=float)

            if winner in timeStage:
                print(f'el ganador de la ronda {i} fue {o}')


cyclists = ['Pere Porcar', 'Joan Beltran', 'Lledó Fabra']
times = np.array([10092.0, 12473.1, 13732.3, 10232.1, 10332.3,
                  11726.2, 11161.2, 12272.1, 11292.0, 12534.0,
                  101934.4, 10292.1, 11712.9, 10133.4, 11632.0]).reshape(3, 5)
stage = 3
print('el ganador de la carrera fue: ', winner(cyclists, times), '\n\n')
print('el ganador de la etapa', stage, 'fue: ',
      stageWinner(cyclists, times, stage), '\n\n')
print(winnerEcahStage(cyclists, times))
