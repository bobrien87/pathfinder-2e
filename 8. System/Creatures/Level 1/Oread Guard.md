---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Oread Guard"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Oread"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common, Petran, Pyric, Sussuran, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +7, Crafting +3, Deception +6, Diplomacy +7, Medicine +5, Occultism +4, Performance +7, Society +4, Survival +5"
abilityMods: ["+2", "+2", "+0", "+1", "+0", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +3, **Ref** +5, **Will** +5"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +9 (`pf2:1`) (two hand d12), **Damage** 1d8+4 slashing"
  - name: "Melee strike"
    desc: "Light Hammer +6 (`pf2:1`) (agile, thrown 20), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Vicious Blow"
    desc: "`pf2:2` **Effect** The oread guard makes a melee Strike. This counts as two attacks when calculating the guard's multiple attack penalty. If this Strike hits, the oread guard deals an extra die of weapon damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Elemental earth laces through the bones of oreads, who appear similar to stone statues of their mortal ancestry, with delicate crystals in place of hair, fur, or scales. Most oreads are stoic and slow to plan but steadfast in their resolve and unwavering in their convictions.

The typical oread cherishes quiet seclusion. Yet as they age, many oreads find themselves inexplicably drawn to some far-flung location with a pull like that exerted on the needle of a compass—intangible, constant, and ultimately irresistible. The destination of this mysterious pilgrimage is unique to each oread, though it usually ends in some place of great mystical power, natural splendor, or esoteric learning. Most oreads are drawn to a place that's somewhat familiar, but a rare few feel drawn to travel in a seemingly random direction, departing with only the hope that they'll discover whatever mystery lies at the end of their invisible path.

Many oreads find that the role of a guard suits their personality well, for in such a role they can feel as if they're helping promote order but also find time to stand vigil as lone sentinels over a specific portion of a fortification or a remote location on a wilderness trail.

```statblock
creature: "Oread Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
