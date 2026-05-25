---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Roc"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +21"
abilityMods: ["+8", "+2", "+5", "-4", "+1", "+0"]
abilities_top:
  - name: "Carry"
    desc: "A roc can Fly at half Speed while it has a creature [[Grabbed]] or [[Restrained]] in either or both of its talons, carrying that creature along with it."
  - name: "Snack"
    desc: "A roc gains a +2 circumstance bonus to hit with its beak Strike if the target is [[Grabbed]] or [[Restrained]] in its talon."
armorclass:
  - name: AC
    desc: "27; **Fort** +20, **Ref** +17, **Will** +16"
health:
  - name: HP
    desc: "180"
abilities_mid:
  - name: "Wing Rebuff"
    desc: "`pf2:r` **Trigger** A creature moves from beyond the reach of the roc's wing to within the reach of the roc's wing. <br>  <br> **Effect** The roc makes a wing Strike against the triggering creature. If the roc Pushes the creature, it disrupts the triggering move action."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Improved Push 10 feet"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +21 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d10+12 piercing"
  - name: "Melee strike"
    desc: "Talon +21 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 2d8+12 slashing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Wing +21 (`pf2:1`) (agile, reach 30 ft.), **Damage** 2d6+10 bludgeoning plus [[Improved Push]]"
spellcasting: []
abilities_bot:
  - name: "Flying Strafe"
    desc: "`pf2:2` The roc Flies up to its Speed and makes two talon Strikes at any point during that movement. Each Strike must target a different creature. Each attack takes the normal multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These legendary, massive raptors, capable of carrying off elephants as prey, are typically about 30 feet long from beak to tail and have a wingspan of 80 feet or more. While their beaks are hooked to rip flesh from bone, their hunting strategy involves grabbing their prey in their powerful talons and then dropping it from great heights before feeding. This method creates a massive amount of carrion, which guarantees that rocs are followed by flocks of opportunistic scavengers, such as ravens and buzzards, who find it easy to steal bits of the larger birds' meals. Rocs, for the most part, don't mind these creatures, which sometimes get gobbled up along with the rest of the roc's food.

Rocs usually nest among mountaintops and cliffs inaccessible to all but the bravest of terrestrial dwellers. They are long-range predators that hunt both land and sea in search for massive prey to sustain them and their young. Rocs are antisocial and lone hunters who compete with each other in fierce aerial battles to protect territory. But about once a decade, a mating couple pairs up to raise their chicks. Once the chicks are old enough to hunt on their own, the parents separate to once again engage in lone hunting.

Particularly skilled druids or rangers might capture and train a roc to serve as a flying mount or hunting companion, though examples of such an incredible feat of domestication are few and far between. The easiest way to rear a roc is to do so from the moment it hatches, since the chick imprints on the first creature it sees. Acquiring a roc egg is by no means an easy feat, though, and is often a death sentence for the would-be egg-snatcher.

```statblock
creature: "Roc"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
