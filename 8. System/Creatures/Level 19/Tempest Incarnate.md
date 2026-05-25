---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tempest Incarnate"
level: "19"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29"
languages: "Common, Sussuran, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +35, Intimidation +37, Nature +34, Stealth +35, Survival +31"
abilityMods: ["+2", "+5", "+3", "+1", "+4", "+6"]
abilities_top:
  - name: "Wind Rider"
    desc: "A tempest incarnate ignores penalties and difficult terrain from strong winds. When flying, they don't need to [[Fly]] each round to avoid falling."
  - name: "Intimidating Storm"
    desc: "A creature that fails a saving throw against a [[Cataclysm]] or [[Wrathful Storm]] spell cast by the tempest incarnate becomes [[Frightened]] 2 (or [[Frightened]] 3 on a critical failure). A creature can only be frightened once by each casting of *wrathful storm*."
  - name: "Swiftness"
    desc: "The tempest incarnate's movement doesn't trigger reactions."
armorclass:
  - name: AC
    desc: "40; **Fort** +30, **Ref** +34, **Will** +31"
health:
  - name: HP
    desc: "360; **Resistances** cold 15, electricity 20"
abilities_mid:
  - name: "Earthbound Vulnerability"
    desc: "A tempest incarnate who is hit by or fails a saving throw against an effect that prevents them from flying (such as [[Earthbind]] or Felling Strike) takes 20 mental damage in addition to the usual effects."
  - name: "Hurricane Cloak"
    desc: "10 feet. A creature that enters the area must succeed at a DC 38 [[Athletics]] check (if on the ground) or Acrobatics check to `act maneuver-in-flight dc=38` (if flying) or end its movement. A creature that critically fails is also knocked back 5 feet and falls [[Prone]]. Creatures making ranged projectile and thrown attacks that pass through the area must succeed on a DC 5 flat check or the attack fails. Massive projectiles, such as thrown boulders, are not affected. A tempest incarnate can activate or deactivate this ability with a single action that has the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +32 (`pf2:1`) (agile, finesse, magical, nonlethal, unarmed), **Damage** 3d4+8 bludgeoning plus 3d12 electricity plus [[Push]]"
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 44, attack +37<br>**10th** (1 slots) [[Cataclysm]]<br>**9th** (4 slots) [[Detonate Magic (Items That Grant Flight Only)]], [[Wrathful Storm]]<br>**8th** (4 slots) [[Arctic Rift]]<br>**7th** (4 slots) [[Unfettered Pack]]<br>**6th** (4 slots) [[Chain Lightning]], [[Field of Life]], [[Truesight]]<br>**5th** (4 slots) [[Control Water]]<br>**4th** (4 slots) [[Fly]], [[Hydraulic Torrent]], [[Unfettered Movement]]<br>**3rd** (4 slots) [[Haste]], [[Wall of Wind]]<br>**2nd** (4 slots) [[Environmental Endurance]], [[Mist]], [[Water Breathing]]<br>**1st** (4 slots) [[Air Bubble]], [[Caustic Blast]], [[Electric Arc]], [[Frostbite]], [[Gust of Wind]], [[Know the Way]], [[Sigil]]"
abilities_bot:
  - name: "Push 10 Feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

When a sorcerer's blood calls to storm and sky, they can become a frightening force to behold. When that power matures, they become living conduits of the tempest.

A primalist is a wielder of primal energies and magic, sometimes taught by forces of primal power, including powerful elementals or fey of the First World. Primalists protect the natural world, offering strong medicine to those in need while facing suspicion from those who don't understand their ways.

A great many primalists belong to druidic circles, and even those who aren't members tend to be familiar with the most prominent ones in their homeland.

```statblock
creature: "Tempest Incarnate"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
