---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Earth Wisp"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +6, Dungeon Lore +4, Plane of Earth Lore +4"
abilityMods: ["+2", "+1", "+3", "+0", "+2", "+0"]
abilities_top:
  - name: "In Concert"
    desc: "When an earth wisp rolls a critical failure on a check to [[Aid]], they get a failure instead, and when they roll a success, they get a critical success instead."
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +5, **Will** +4"
health:
  - name: HP
    desc: "15; **Immunities** bleed, paralyzed, poison, sleep; **Resistances** bludgeoning 2"
abilities_mid:
  - name: "Accord Essence"
    desc: "`pf2:r` **Trigger** An ally within 30 feet that benefited from the wisp's resonance in the last hour is targeted by an attack <br>  <br> **Effect** The wisp detonates themself in an elemental explosion. This grants temporary Hit Points equal to half the wisp's current Hit Points to allies within @Template[emanation|distance:30]{30 feet} who have benefited from the wisp's resonance in the last hour. These temporary Hit Points last 1 hour. <br>  <br> A wisp that uses this reaction is permanently destroyed, and they can be restored by only a [[Wish]] ritual or similarly powerful effect. If an ability would prevent the wisp's destruction (for instance, if the wisp is summoned and would merely be dismissed), Accord Essence has no effect."
  - name: "Resonance"
    desc: "30 feet. All wisps vibrate at a frequency attuned to their element, resonating with and empowering all creatures and effects sharing that trait. <br>  <br> A creature in the area gains a +1 status bonus to attack and damage rolls for effects with the earth trait; a creature with the elemental and earth traits gains this bonus to all attack and damage rolls."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +6 (`pf2:1`) (reach 10 ft.), **Damage** 1d4+2 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Earth wisps are rolling spheres of rock, mud, and leaves, perpetually humming with low, rumbling energy. They're timid and aloof but fiercely loyal to those they know and trust.

Wisps are tiny elemental beings that emerged during the creation of the Elemental Planes. The first wisps roamed the Inner Sphere in shifting symphonies that traded members with their every meeting. These symphonies of free wisps created music out of their combined resonances, but when the wicked Elemental Lords realized the value of the wisps' resonance, they captured whole symphonies for use as servants.

Wisps attune to each other and to those they surround themselves with. This attunement makes them naturally supportive allies. Free wisps still roam the Inner Sphere and the Universe, but they're usually shy and hide themselves from strangers. However, they happily offer their service to those who show them kindness. They especially find themselves drawn to spellcasters who practice elemental magic; these wisps usually watch from afar but sometimes approach those who seem safe to become familiars or comrades.

Free wisps who find one another become close almost immediately. They get especially excited when they find wisps of elements other than their own, showing none of the animosity sometimes exhibited between elementals of different planes. Instead, they join in an excited dance, emitting resonances that faintly echo the symphonies of ancient days.

```statblock
creature: "Earth Wisp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
