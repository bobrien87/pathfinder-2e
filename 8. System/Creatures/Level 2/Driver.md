---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Driver"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +7, Deception +7, Intimidation +7, Stealth +8, Driving Lore +8, Engineering Lore +8, Piloting Lore +8"
abilityMods: ["+1", "+4", "+0", "+2", "+2", "+1"]
abilities_top:
  - name: "Driving Specialist"
    desc: "For encounters involving driving, the driver is an 8th-level challenge."
  - name: "Express Driver"
    desc: "A driver can attempt a Driving lore check to increase a vehicle's travel Speed when calculating the value for a day. The DC is determined by the GM but is typically based on the vehicle's piloting DC or the difficulty of traversing the environment, whichever is harder. On a success, increase the vehicle's travel Speed by half."
  - name: "Skilled Driver"
    desc: "The driver gains a +10 circumstance bonus to any skill check involved in driving a vehicle, and is considered a master in the skill for such checks. This bonus also applies to any initiative roll while the driver is piloting a vehicle."
armorclass:
  - name: AC
    desc: "18 +6 status to all defenses while driving; **Fort** +6, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "+6 Status to All Defenses While Driving"
    desc: ""
  - name: "Vehicle Block"
    desc: "`pf2:r` **Requirements** The driver is driving a vehicle <br>  <br> **Trigger** The driver would take damage from an attack or from a damaging effect that requires a Reflex save <br>  <br> **Effect** With swift steering, the driver puts the bulk of the vehicle in between themself and the problem, causing the vehicle to take the damage instead of the driver."
  - name: "Sideswipe"
    desc: "`pf2:r` **Requirements** The driver is taking a Drive action with a vehicle and moves the vehicle adjacent to a creature <br>  <br> **Effect** All creatures adjacent to the vehicle take the vehicle's collision damage with a [[Reflex]] save against the vehicle's collision DC. The vehicle continues to move normally after the Sideswipe."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Crowbar +7 (`pf2:1`) (fatal d10), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

With daring and charm, a driver is a professional operator of mechanical vehicles. Their skill and recklessness give them a reputation that puts even the quickest horse riders to shame. A driver's vehicle becomes an extension of themselves, allowing the driver to perform near-impossible feats of maneuverability. Drivers have other tricks up their sleeve, as their charm is undeniable. When needed, they can talk, lie, or frighten their way out of a bumpy situation in and out of a vehicle.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Driver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
