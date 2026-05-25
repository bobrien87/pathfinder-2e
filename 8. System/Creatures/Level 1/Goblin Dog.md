---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Goblin Dog"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +7"
abilityMods: ["+3", "+2", "+2", "-4", "+1", "-1"]
abilities_top:
  - name: "Goblin Pox"
    desc: "Goblins and goblin dogs are immune to goblin pox. <br>  <br> **Saving Throw** DC 17 [[Fortitude]] save <br>  <br> **Stage 1** [[Sickened]] 1 (1 round) <br>  <br> **Stage 2** sickened 1 and [[Slowed]] 1 (1 round) <br>  <br> **Stage 3** [[Sickened]] 2 and can't reduce its sickened value below 1 (1 day)"
armorclass:
  - name: AC
    desc: "15; **Fort** +8, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "17"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 17 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
  - name: "Irritating Dander"
    desc: "A creature that hits the goblin dog with an unarmed attack, tries to [[Grapple]] it, or otherwise touches it is exposed to goblin pox."
  - name: "Juke"
    desc: "`pf2:r` **Requirements** A creature must be mounted on the goblin dog. <br>  <br> **Trigger** The rider issues a command to the goblin dog. <br>  <br> **Effect** The goblin dog Steps before following the command."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (unarmed), **Damage** 1d6+3 piercing plus [[Goblin Pox]]"
spellcasting: []
abilities_bot:
  - name: "Scratch"
    desc: "`pf2:2` The goblin dog vigorously scratches itself, exposing all adjacent creatures to goblin pox."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Goblins' eponymous pets aren't true canines at all but rather large, blunt-nosed rodents with thin bodies and long legs. Often as cowardly as they are ugly, goblin dogs prefer to lurk behind bushes or in deep shadows, only pouncing upon lone or wounded prey. Goblin dogs frequently roam in packs, but they are likely to flee from a fight if injured, even if it means abandoning their packmates.

Goblin dogs take their name from a long association with goblins, who breed the beasts as guard animals and mounts. Most goblins take issue with the name, as the average goblin is appalled at the suggestion that their favored mounts have anything at all to do with actual dogs. Of course, being goblins, they haven't bothered to come up with their own unique name for the creatures.

Even the most pampered goblin dogs have itchy mange and prolific dander that tenaciously affects those who come in contact with them. This "goblin pox" causes itchy hives and festering sores that are as unsightly as they are irritating and distracting. Goblin dog dander causes allergic reactions in nearly all other creatures that don't share goblin dogs' terrible hygiene—with the notable exception being, of course, goblins, who remain entirely immune to the disease regardless of cleanliness.

Hunger can drive goblin dogs to bouts of uncharacteristic violence, and crueler goblins sometimes purposefully starve their pets on the eve of battle. Goblin dogs subsist on whatever organic material they can scavenge; they particularly enjoy fresh carrion. Although goblins are far from picky eaters themselves, they value goblin dogs because the noisome animals will consume material that even goblins won't touch. In fact, "Will It Eat?" is one of the most popular games goblins play with their pets, where a wide range of morsels (not always edible or safe to consume) are dangled before a goblin dog's snout. Sadly, the game "Will It Die?" is often played after "Will It Eat?" Goblin dogs that survive the second game earn renown for their digestive prowess and often become favored tribal pets, treated even better than most of the rank-and-file goblins.

```statblock
creature: "Goblin Dog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
