---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeletal Titan"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +28"
abilityMods: ["+9", "+3", "+4", "-5", "+2", "-1"]
abilities_top:
  - name: "Bone Debris"
    desc: "The bones a skeletal titan throws are large enough to clutter the battlefield. When the skeletal titan hits a creature with a bone attack, the projectile becomes difficult terrain in the square the creature occupies (or, if the creature occupies more than one square, one square it occupies of the titan's choice). If the titan misses with a bone attack, instead a random square adjacent to the creature becomes difficult terrain."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +24, **Will** +21"
health:
  - name: HP
    desc: "210; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Resistances** cold 10, electricity 10, fire 10, piercing 15, slashing 15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mountain Sword +26 (`pf2:1`) (reach 20 ft.), **Damage** 3d12+13 bludgeoning"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 3d8+13 bludgeoning"
  - name: "Melee strike"
    desc: "Foot +26 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 3d8+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Bone +24 (`pf2:1`) (brutal, range 60 ft.), **Damage** 2d10+13 bludgeoning plus [[Bone Debris]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 31, attack +21<br>**4th** [[Fly]] (Constant)"
abilities_bot:
  - name: "Mountain Slam"
    desc: "`pf2:3` The skeletal titan slams its mountain sword into the ground. The shock wave reverberates, dealing @Damage[(3d12+13)[bludgeoning]|options:area-damage] damage to all creatures in a @Template[type:line|distance:20] (DC 33 [[Reflex]] save). A creature that fails its save is also knocked [[Prone]]."
  - name: "Trample"
    desc: "`pf2:3` Huge or smaller, foot, DC 33 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Only the powerful and foolish would raise the bones of a mighty titan or similarly gargantuan creature as a skeleton. Skilled practitioners see this as a waste of a powerful body and instead imbue them with magic that allows them to fly. The wise know it's nearly impossible to control such a colossus and that it's just as likely to crush its creator underneath its mighty foot as it is to smite their foes.

Among the ranks of the dead, none are so numerous, nor so varied, as the skeleton. While most are almost entirely made from bone, some maintain a few scraps of flesh to aid them in movement, such as wing membranes.

```statblock
creature: "Skeletal Titan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
