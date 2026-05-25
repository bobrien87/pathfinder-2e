---
type: creature
group: ["Ghost", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ghost Mage"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Ghost"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Arcana +22, Intimidation +22, Stealth +21"
abilityMods: ["-5", "+3", "+0", "+6", "+3", "+6"]
abilities_top:
  - name: "Site Bound"
    desc: "A typical ghost can stray only a short distance from where it was killed or the place it haunts. A typical limit is 120 feet. Some ghosts are instead bound to a room, building, item, or creature that was special to it rather than a location."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "135; rejuvenation, void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 10 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Rejuvenation"
    desc: "Completing the ghost mage's project allows it to move on to the afterlife. <br>  <br> When a ghost is destroyed, it re-forms after 2d4 days within the location it's bound to, fully healed. A ghost can be permanently destroyed only if someone determines the reason for its existence and sets right whatever prevents the spirit from resting."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ghostly Hand +21 (`pf2:1`) (agile, finesse, magical), **Damage** 2d8+12 void"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 29, attack +23<br>**5th** [[Hallucination]], [[Howling Blizzard]]<br>**4th** [[Suggestion]], [[Vision of Death]]<br>**3rd** [[Blindness]], [[Veil of Privacy]]<br>**2nd** [[Dispel Magic]], [[Telekinetic Maneuver]]<br>**1st** [[Detect Magic]], [[Enfeeble]], [[Figment]], [[Prestidigitation]], [[Read Aura]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Frightful Moan"
    desc: "`pf2:1` The ghost laments its fate, forcing each living creature within @Template[emanation|distance:30]{30 feet} to attempt a DC 29 [[Will]] save. On a failure, a creature becomes [[Frightened]] 2 (or [[Frightened]] 3 on a critical failure). On a success, a creature is temporarily immune to this ghost's frightful moan for 1 minute."
  - name: "Telekinetic Assault"
    desc: "`pf2:2` The ghost cries out in pain and anguish as small objects and debris fly about in a @Template[emanation|distance:30]. Creatures in this area take @Damage[6d6[bludgeoning]|options:area-damage] damage, subject to a DC 29 [[Reflex]] save."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A wizard who died with work incomplete might become a ghost mage.

When some mortals die through tragic circumstances or without closure, their souls can linger and haunt a locale significant to them in life.

```statblock
creature: "Ghost Mage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
