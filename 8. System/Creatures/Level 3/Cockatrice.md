---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cockatrice"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11"
abilityMods: ["-2", "+4", "+1", "-3", "+1", "-1"]
abilities_top:
  - name: "Calcification"
    desc: "A peck from a cockatrice hardens the flesh of the creature struck. The target must succeed at a DC 20 [[Fortitude]] save or become [[Slowed]] 1 (or [[Slowed]] 2 on a critical failure). Further failed saves against calcification increase the slowed condition. Once a creature's actions are reduced to 0 by calcification, that creature becomes [[Petrified]]. If the creature isn't petrified, the slowed conditions end once 1 minute passes without the creature failing a save against calcification. <br>  <br> Every 24 hours after it was petrified, the victim can attempt a DC 20 [[Fortitude]] save to recover. On a success, it becomes flesh again, but is slowed 1 for the next 24 hours. On a critical success, the creature recovers and isn't slowed. On a failure, the creature remains petrified but can try again in 24 hours. On a critical failure, the petrification is permanent, and the creature can't attempt any more saves."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +11, **Will** +6"
health:
  - name: HP
    desc: "45; **Immunities** petrified"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +13 (`pf2:1`) (finesse, magical, unarmed), **Damage** 1d8-2 piercing plus [[Calcification]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Ugly and aggressive, the dread cockatrice stalks garbage pits and hillside dumps in search of prey that it can turn to stone with its petrifying beak and subsequently consume piece by broken piece. Cockatrices resemble gaunt and sickly roosters with bat wings and serpentine tails, and they rarely grow more than 2 feet tall and twice as long. Their absentminded clucking gives smart prey ample warning of their presence, and when angered cockatrices let out a shrill crow like that of a rooster. Their peck releases a magical toxin that causes flesh to quickly calcify, and any creature pecked repeatedly by an irritable cockatrice eventually transforms into a stone statue of itself.

The first cockatrice is rumored to have hatched from a rooster's egg incubated on a dung hill by a toad. Whether or not the rumor is true, the cockatrice's monstrous appearance certainly doesn't contradict its strange and filthy origin story, and these creatures are more than capable of propagating on their own. Cockatrices are remarkably fecund and gather in flocks of up to a dozen members. Each flock contains only a few females. The males—which differ in appearance from the females by having warty wattles and gnarled combs—often fight with each other, with lower-ranking males eventually driven away to find their own lairs or compete among other flocks. Most creatures who run afoul of a solitary cockatrice do so with one of these surly outcasts.

Cockatrice lairs are often littered with fragments of statuary from past victims, although these are as likely to be remnants of lizards and insects as people. Curiously, weasels and ferrets, which infiltrate cockatrice lairs to steal eggs, are immune to the creatures' petrifying bites. For unknown reasons, cockatrices are terrified of and enraged by roosters, and they are equally likely to flee or attack one when confronted.

Particularly brave (or foolhardy) individuals sometimes keep cockatrices as pets or guard animals. In their natural habitat among plains, forests, and sewers near humanoid settlements, cockatrices are content to live off vermin or scraps of waste, but their greatest pleasure is consuming warm meals of freshly petrified flesh.

```statblock
creature: "Cockatrice"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
