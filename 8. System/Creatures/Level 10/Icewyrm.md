---
type: creature
group: ["Amphibious", "Cold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Icewyrm"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Cold"
trait_03: "Elemental"
trait_04: "Water"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Athletics +21"
abilityMods: ["+7", "+7", "+5", "-1", "+5", "+3"]
abilities_top:
  - name: "Ice Burrow"
    desc: "The Icewyrm can Burrow through ice or snow with a Speed of 20 feet. It moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "30; **Fort** +20, **Ref** +21, **Will** +17"
health:
  - name: HP
    desc: "185; **Immunities** bleed, cold, paralyzed, poison, sleep; **Weaknesses** fire 10"
abilities_mid:
  - name: "Explosion"
    desc: "When the icewyrm dies, it explodes, dealing @Damage[8d6[cold]|options:area-damage] damage to each creature in a @Template[type:emanation|distance:10] (DC 27 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +23 (`pf2:1`) (reach 15 ft.), **Damage** 2d12+13 piercing"
  - name: "Melee strike"
    desc: "Tail +23 (`pf2:1`) (agile, reach 15 ft.), **Damage** 2d6+13 slashing plus 1d6 cold"
  - name: "Ranged strike"
    desc: "Ice Shard +23 (`pf2:1`) (cold, range 60 ft.), **Damage** 1d6+13 piercing plus 1d6 cold"
spellcasting: []
abilities_bot:
  - name: "Breathe Ice Shards"
    desc: "`pf2:2` The icewyrm breathes a @Template[type:line|distance:60] of freezing shards of razor-sharp ice, dealing @Damage[3d12[cold],3d12[piercing]|options:area-damage] damage to every creature in the line (DC 29 [[Reflex]] save). The icewyrm can't use Breathe Ice Shards again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Resembling wingless, serpentine dragons formed of jagged ice and shot through with veins of nearly frozen water, these elementals dwell within icebergs and enjoy striking out at passing ships or creatures. They're especially common in frigid stretches of ocean in the Plane of Water, where icebergs cluster together into enormous islands of ice.

Water elementals that become infused with cold or mist have increased mobility in regions outside of bodies of water.

```statblock
creature: "Icewyrm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
