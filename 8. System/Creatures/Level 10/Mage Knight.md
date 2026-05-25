---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mage Knight"
level: "10"
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
    desc: "+17"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +22, Athletics +21, Warfare Lore +20"
abilityMods: ["+5", "+1", "+2", "+4", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "29; **Fort** +18, **Ref** +13, **Will** +21"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Reflex +16 Against Damaging Effects"
    desc: ""
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +21 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Melee strike"
    desc: "Mace +22 (`pf2:1`) (magical, shove), **Damage** 2d6+11 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 28, attack +20<br>**5th** (3 slots) [[Force Barrage]], [[Impaling Spike]], [[Toxic Cloud]]<br>**4th** (3 slots) [[Fireball]], [[Fly]], [[Weapon Storm]]<br>**3rd** (3 slots) [[Earthbind]], [[Vampiric Feast]], [[Wall of Thorns]]<br>**2nd** (3 slots) [[Invisibility]], [[Invisibility]], [[Mist]]<br>**1st** (3 slots) [[Enfeeble]], [[Fleet Step]], [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Electric Arc]], [[Frostbite]], [[Light]], [[Read Aura]], [[Telekinetic Hand]], [[Telekinetic Projectile]]"
  - name: "Wizard Focus Spells"
    desc: "DC 28, attack +20<br>**4th** [[Energy Absorption]]<br>**1st** [[Force Bolt]]"
abilities_bot:
  - name: "Bespell Strikes"
    desc: "`pf2:0` **Frequency** once per turn <br>  <br> **Requirements** The mage knight's most recent action was to cast a non-cantrip spell <br>  <br> **Effect** The mage knight siphons spell energy into one weapon they're wielding, or into one of their unarmed attacks. Until the end of the turn, the weapon or unarmed attack deals an extra 2d6 force damage and gains the arcane trait if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead"
  - name: "Drain Bonded Item"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Requirements** The mage knight hasn't acted yet on this turn <br>  <br> **Effect** The mage knight expends the power stored in their bonded item (typically their shield). This gives them the ability to cast one prepared spell they prepared today and already cast, without spending a slot."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Though many spellcasters prefer to defend themselves with magic, some recognize that there's no substitute for a suit of steel. Mage knights defy the stereotype that spellcasters are frail, delicate, and passive and instead choose to hold their own in close-quarter combat.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Mage Knight"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
