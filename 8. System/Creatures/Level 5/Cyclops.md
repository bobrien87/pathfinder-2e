---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cyclops"
level: "5"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Cyclops, Jotun"
skills:
  - name: Skills
    desc: "Athletics +14, Intimidation +10, Survival +12, Fortune-Telling Lore +13"
abilityMods: ["+5", "-1", "+2", "+0", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +8, **Will** +12"
health:
  - name: HP
    desc: "80"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
  - name: "Flash of Insight"
    desc: "`pf2:0` **Frequency** once per day. <br>  <br> **Trigger** The cyclops is about to roll a d20. <br>  <br> **Effect** The cyclops peers into an occluded spectrum of possible futures. It gets a success (but not a critical success) on the roll instead of rolling."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +14 (`pf2:1`) (reach 10 ft., sweep), **Damage** 1d12+9 slashing"
  - name: "Ranged strike"
    desc: "Heavy Crossbow +8 (`pf2:1`) (reload 2, range 120 ft.), **Damage** 1d10+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Swipe"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The cyclops makes a melee Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within their melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. A Swipe counts as two attacks for the cyclops's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The kingdoms of the cyclopes date to an age before the rise of humanity, when dragons and giants and serpentfolk ruled the world. The cyclopes built enormous stone cities and prayed to ancient gods of brutality and wrath, but their power to foresee the future failed them and their civilization collapsed. Today, most cyclopes have virtually no knowledge of the former glory of their kind, even though it is not uncommon for them to dwell among the ruins of their greatness. Cyclops cities include monuments and imposing murals which depict their peoples' history, but few now among them can read or interpret these relics of the past.

In addition to their single eye, cyclopes are also famous for their neverending hunger, an appetite so all-consuming that some scholars theorize it may in fact be some kind of curse. The ever-present hunger of the cyclopes seems to have some connection to the death of their civilization—though whether this voracity was the cause or a side-effect of their people's downfall is likely destined to remain a mystery.

Although details of the cyclopes' gods have largely been lost to the annals of time, what little is known about these deities suggests they were vindictive and petty enough to curse their own people if they felt neglected or badly served.

The cyclopes are violent giants with a tragic past. Although they possess only one eye, they could once see far more than most, possessing occult wisdom and divinatory magic that gave them the mystic ability of foresight. But their legendary oracular powers failed to prevent the fall of their society, and the vast kingdoms of the cyclops long ago collapsed into ruin. Today, cyclopes have forgotten much of what they once knew, and they skulk among the crumbling remains of their fallen cities like forgotten kings and queens of their own fallen kingdoms.

```statblock
creature: "Cyclops"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
