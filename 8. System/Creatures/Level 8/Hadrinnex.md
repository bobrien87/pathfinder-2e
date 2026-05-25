---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hadrinnex"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: "Aklo (telepathy (touch))"
skills:
  - name: Skills
    desc: "Acrobatics +16, Athletics +18, Occultism +11"
abilityMods: ["+6", "+4", "+6", "-3", "+3", "-3"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +14, **Will** +17"
health:
  - name: HP
    desc: "118"
abilities_mid:
  - name: "Rapid Evolution"
    desc: "`pf2:r` **Trigger** The hadrinnex takes damage of a physical or energy damage type (bludgeoning, piercing, or slashing for physical; acid, cold, electricity, fire, force, sonic, or void for energy) <br>  <br> **Effect** The hadrinnex reconfigures its husk (if triggered by physical damage) or its energy gland (if triggered by energy damage). Any reconfiguration applies to the triggering damage and lasts until the next time the hadrinnex uses Rapid Evolution. <br>  <br> - **Energy Gland** Reconfiguring the energy gland changes both the hadrinnex's energy damage resistance and the damage of its energy ray to that type. By default, the energy gland is configured to sonic. <br>  <br> - **Husk** The hadrinnex's physical damage resistance and the damage of its weapon arm Strikes change to the triggering type. Weapon arm Strikes gain an additional trait depending on the current damage type: bludgeoning adds shove, piercing adds deadly d8, and slashing adds sweep. By default the husk is configured to bludgeoning."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Weapon Arm +20 (`pf2:1`) (reach 10 ft.), **Damage** 2d8 + 9 untyped"
  - name: "Ranged strike"
    desc: "Energy Ray +18 (`pf2:1`) (occult), **Damage** 5d6 untyped"
spellcasting: []
abilities_bot:
  - name: "Extend Limbs"
    desc: "`pf2:2` The hadrinnex makes two weapon arm Strikes, each targeting a different creature. The hadrinnex's reach increases to 20 feet for these Strikes."
  - name: "Vent Energy"
    desc: "`pf2:1` The hadrinnex purges the energy in its energy gland for an external discharge. <br>  <br> It either blasts the energy to deal @Damage[7d6[@actor.flags.system.energyGland.type]|options:area-damage] damage to creatures in a @Template[cone|distance:30] (DC 26 [[Reflex]] save), or directs the energy to its weapon arms, making its weapon arm Strikes deal an extra 2d6 energy damage for 1 minute. <br>  <br> Either one expends the damage type stored in the hadrinnex's energy gland, as described below. <br>  <br> After the energy is vented, the energy gland goes dormant. The hadrinnex loses its energy resistance and can't use energy ray until it uses Rapid Evolution to reconfigure its energy gland again. Directing energy to its weapon arms again removes any previous energy boost to its weapon arm. <br>  <br> > [!danger] Effect: Vent Energy"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The bizarre hadrinnexes resemble defensive systems more than living creatures. They evolve at a rapid rate, but only to specific attacks against them, which suggests they were created through advanced technology or magic. The husk surrounding a hadrinnex-flecks of metal suspended in a malleable organic carapace-reshapes in response to harm. So too can a glowing gland within the creature's thorax, which collects energy and restructures the creature's biology to protect it from that energy. This organ is fragile and ruptures soon after a hadrinnex is killed.

Hadrinnexes have only a rudimentary intellect and usually follow more intelligent aberrations. As bodyguards or peons, they perform simple tasks diligently. Though poor at problem-solving and improvisation, hadrinnexes' dependability and adaptive physiology make them ideal for dangerous tasks in hazardous environments.

```statblock
creature: "Hadrinnex"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
