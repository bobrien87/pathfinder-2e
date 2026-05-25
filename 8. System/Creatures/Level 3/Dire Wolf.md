---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dire Wolf"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +10, Stealth +8, Survival +10"
abilityMods: ["+5", "+3", "+4", "-4", "+3", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The dire wolf's Strikes deal 1d6 extra damage to creatures within reach of at least two of the wolf's allies."
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +8, **Will** +8"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 20 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 1d10+5 piercing plus [[Grab]] plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Worry"
    desc: "`pf2:1` **Requirements** The dire wolf has a creature [[Grabbed]] or [[Restrained]] in its jaws <br>  <br> **Effect** The dire wolf fiercely shakes the creature with its teeth, dealing @Damage[(1d10+2)[piercing]] damage with a DC 20 [[Fortitude]] save."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Much larger and more foul-tempered than their common cousins, dire wolves haunt primeval lands that accommodate their massive size and proportionately large hunting grounds and appetites. Orcs are fond of using dire wolves as mounts, finding their vicious tempers perfect for hunting and warfare. Dire wolves are far more likely to prey on humanoids than ordinary wolves, considering them nothing but another kind of smaller, nutritious animal.

Wolves roam forests, hills, and other wild lands, where they hunt in packs to beleaguer and surround their prey before going in for the kill. Like most predatory animals, wolves prefer to attack the weakest or most vulnerable prey they can find.

```statblock
creature: "Dire Wolf"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
