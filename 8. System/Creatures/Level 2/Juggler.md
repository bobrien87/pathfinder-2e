---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Juggler"
level: "2"
rare_01: "Common"
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
    desc: "+9"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Performance +11, Circus Lore +8"
abilityMods: ["+2", "+3", "+1", "+0", "+1", "+3"]
abilities_top:
  - name: "Juggling Specialist"
    desc: "For encounters involving juggling and other circus acts, the juggler is a 5th-level challenge."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Return Throw"
    desc: "`pf2:r` **Trigger** A physical ranged attack with a throwing weapon critically fails to hit the juggler <br>  <br> **Effect** The juggler snatches the weapon from the air and immediately makes a ranged Strike against the attacker using that weapon."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dart +10 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Torch +10 (`pf2:1`) (thrown 10), **Damage** 1d4+4 bludgeoning plus 1 fire"
  - name: "Melee strike"
    desc: "Juggling Club +9 (`pf2:1`) (agile), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Juggling Club +10 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Juggle"
    desc: "`pf2:1` The juggler begins juggling up to three items of light or negligible Bulk. They can choose items in their hands or Interact to draw items on their person or pick up unattended items in reach. While juggling, they can Interact to add up to two items to their juggle, though they must drop an item for each one they add. The juggler is wielding all items they juggle, but the only actions they can take that require their hands are Return Throw, Juggling Bounce, Strike using a juggled weapon, Interact to add items to their juggle, or Dismiss to stop juggling. <br>  <br> When the juggler Dismisses Juggle, they can choose to continue to wield, drop, or stow each juggled item, though they can't wield more items than they have hands. If at any point the juggler isn't wielding any items or becomes [[Restrained]] or [[Unconscious]], the juggle ends and the juggler drops all the items."
  - name: "Juggling Bounce"
    desc: "`pf2:1` The juggler Strikes with a thrown weapon they're juggling. If the Strike hits, the weapon bounces to a different creature in the weapon's first range increment. The juggler repeats the Strike, which uses the same multiple attack penalty and doesn't increase their multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Jugglers are physical performers who master the art of manipulating props. Usually, this involves throwing multiple objects up in a flowing pattern, but some use ricocheting items, spinning items, or other objects to keep them aloft.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Juggler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
