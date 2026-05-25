---
type: creature
group: ["Humanoid", "Kobold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kobold Trapper"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +5, Crafting +8, Stealth +7, Survival +7"
abilityMods: ["+1", "+3", "+1", "+3", "+2", "+0"]
abilities_top:
  - name: "+2 to Seek for Traps"
    desc: ""
  - name: "Booby-Trapped"
    desc: "A kobold trapper protects items in their backpack with a booby trap. This booby trap requires a successful DC 18 [[Perception]] check to notice, and two successful DC 15 [[Thievery]] check to disable. <br>  <br> Accessing the backpack without disabling the trap destroys its contents, and splinters explode in a @Template[type:burst|distance:10] centered on the backpack, dealing @Damage[3d6[piercing]|options:area-damage] damage (DC 15 [[Reflex]] save)."
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "32"
abilities_mid:
  - name: "+1 Circumstance to All Defenses vs. Traps"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Hammer +7 (`pf2:1`) (agile), **Damage** 1d6+1 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +9 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+1 bludgeoning"
  - name: "Melee strike"
    desc: "Claw +7 (`pf2:1`) (agile, unarmed), **Damage** 1d4+1 slashing"
  - name: "Ranged strike"
    desc: "Crossbow +9 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing"
spellcasting: []
abilities_bot:
  - name: "Construct Trap"
    desc: "`pf2:3` The kobold trapper creates a rudimentary trap on a surface in an adjacent square. The trap activates the next time a creature moves adjacent to it. The creature takes 2d6 bludgeoning, piercing, or slashing damage (determined by the trapper when the trap is constructed) with a DC 18 [[Reflex]] save. On a failure, the creature also takes a –5 status penalty to all Speeds for 1 minute. The trap is destroyed when activated or after 8 hours, whichever comes first. A trapper typically carries enough raw materials to make six traps each day. <br>  <br> > [!danger] Effect: Construct Trap"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Kobolds are skillful artisans, always inventing new traps and snares to defend their territory and ambush enemies. Kobold trappers enjoy showing off their crafting prowess on the battlefield.

Kobolds are drawn to beings and objects of power, establishing their communities near them. Once a warren has been formed, the resident kobolds construct traps and set up ambushes to deter interlopers.

```statblock
creature: "Kobold Trapper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
