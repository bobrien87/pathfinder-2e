---
type: creature
group: ["Elemental", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ambush Copse"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Elemental"
trait_02: "Plant"
trait_03: "Wood"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Tremorsense]] (imprecise) 30 feet"
languages: "Common, Fey (Muan cant speak any language)"
skills:
  - name: Skills
    desc: "Athletics +27, Intimidation +20, Stealth +23"
abilityMods: ["+8", "+4", "+6", "+0", "+4", "+0"]
abilities_top:
  - name: "Pounding Smash"
    desc: "Regardless of whether the Strike hits or misses, the ambush copse's melee Strikes create a 5-foot-square of difficult terrain in the target's space."
  - name: "Sunder Objects"
    desc: "When an ambush copse damages an item or structure, it deals an additional 15 untyped damage to that item or structure."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +22, **Will** +22"
health:
  - name: HP
    desc: "300; **Weaknesses** fire 15, axe vulnerability 10; **Resistances** bludgeoning 10, piercing 10"
abilities_mid:
  - name: "Berserk"
    desc: "An ambush copse that sees fire or axes has a chance of going berserk. At the start of its turn, if it is aware of an axe or a fre the size of a lit torch or larger, the ambush copse must succeed at a DC 5 flat check or go berserk. A berserk ambush copse can't use concentrate actions and wildly attacks the nearest living creature, or the nearest object if no creatures are nearby."
  - name: "Blinding Branches"
    desc: "`pf2:r` **Trigger** A creature within 20 feet of the ambush copse leaves a square during a move action it's using <br>  <br> **Requirements** The triggering creature is in forest terrain <br>  <br> **Effect** The ambush copse's elemental energy animates nearby tree branches to swat at the creature's face. The triggering creature must succeed at a DC 30 [[Reflex]] save or become [[Blinded]] for 1 round."
  - name: "Felling Ambush"
    desc: "`pf2:r` **Trigger** A creature moves within 10 feet of the ambush copse <br>  <br> **Requirements** The ambush copse is disguised as trees or logs <br>  <br> **Effect** The ambush copse makes a log Strike against the triggering creature. If the attack hits, the creature must attempt a DC 30 [[Reflex]] save or be knocked [[Prone]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Log +27 (`pf2:1`) (backswing, forceful, reach 20 ft., sweep), **Damage** 3d12+14 bludgeoning plus [[Pounding Smash]]"
  - name: "Melee strike"
    desc: "Caber +25 (`pf2:1`) (thrown 40), **Damage** 3d12+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Feign Copse"
    desc: "`pf2:1` Until the next time it acts, the ambush copse appears to be a harmless patch of trees or logs. It has an automatic result of 43 (45 in forests) on Deception checks and DCs to pass as trees or logs."
  - name: "Pulverizing Barrage"
    desc: "`pf2:3` The ambush copse makes three log Strikes, each at a –2 penalty, all targeting the same creature. The ambush copse's multiple attack penalty doesn't increase until after it has made all three attacks. The ambush copse gains the [[Clumsy]] 2 condition until the beginning of its next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sawed and axe-hewn timber grind together as an ambush copse moves, smashing through the forest. Cuts and burns mar the bark of this gigantic, angry mass of whirling, deadly logs.

The forest never forgets. It remembers the hatchets, the rasping saws, and the smoke of crackling wood fres. It remembers the carts taking ancient trees away to cut, shape, and burn. Fey meddling or errant elemental magic draw such memories out alongside the rage and sorrow of the forest to form an ambush copse.

An ambush copse exacts its ire on villages along the woodcutter's path or waits for intruders to step into its forest domain. While an ambush copse might be mistaken for a wounded arboreal, it can cease movement to appear as an overgrown pile of logs or a partially collapsed hovel. There, it waits for retribution.

```statblock
creature: "Ambush Copse"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
