---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Assassin"
level: "8"
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
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +13, Deception +12, Diplomacy +10, Intimidation +10, Medicine +14, Society +12, Stealth +19, Thievery +15, Underworld Lore +14"
abilityMods: ["+3", "+5", "+2", "+2", "+2", "+0"]
abilities_top:
  - name: "Swift Sneak"
    desc: "The assassin can move their full speed when [[Sneaking]]."
  - name: "Sneak Attack"
    desc: "The assassin deals an extra 2d6 precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attack"
    desc: "On the first round of combat, creatures that haven't acted yet are [[Off Guard]] to the assassin."
armorclass:
  - name: AC
    desc: "26; **Fort** +12, **Ref** +19, **Will** +14"
health:
  - name: HP
    desc: "130"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The assassin isn't [[Off Guard]] to creatures of 8th level or lower that are [[Hidden]], [[Undetected]], flanking or using [[Surprise Attack]]."
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The assassin is targeted with a melee or ranged attack by an attacker they can see. <br>  <br> **Effect** The assassin gains a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +20 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 1d6+9 piercing"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +20 (`pf2:1`) (deadly 2d10, magical, propulsive, reload 0, range 60 ft.), **Damage** 2d6+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Assassin's Poison"
    desc: "`pf2:1` **Requirements** The assassin is wielding a piercing or slashing weapon and has a free hand <br>  <br> **Effect** The assassin applies a poison to the weapon. That poison's DC is increased to 24 if it was lower."
  - name: "Quick Draw"
    desc: "`pf2:1` The assassin [[Interacts]] to draw a weapon, then [[Strike|Strikes]] with that weapon."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Assassins commit murder, either for pay or due to their belief in a cause, such as a religion or a political movement. Many are members of assassins' guilds: organizations that accept contracts to kill in return for money, favors, or both.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Assassin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
