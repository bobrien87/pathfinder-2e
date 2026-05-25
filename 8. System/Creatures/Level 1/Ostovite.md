---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ostovite"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]]"
languages: "Chthonian"
skills:
  - name: Skills
    desc: "Crafting +4, Stealth +7"
abilityMods: ["+0", "+4", "+3", "-4", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Bone Chariot"
    desc: "Ostovites build and inhabit moving shells of bone. The ostovite's base statistics, particularly its immunities, assume the ostovite is safely inside its bone chariot. The bone chariot is destroyed when the ostovite is reduced to less than half its Hit Points or immediately after it takes damage from a critical hit. Damage that can specifically affect the ostovite controlling the chariot even while it's inside (such as the spell *spirit blast*) doesn't destroy the bone chariot, and it bypasses the ostovite's immunities. <br>  <br> Without the bone chariot, the ostovite loses its immunities and bone spike Strike, and it is reduced to Tiny size. It also gains weakness 5 to mental and physical damage as well as damage with the holy trait. Building a new bone chariot requires the skeleton of a Small or larger creature and 10 minutes. An ostovite in a bone chariot is normally Small, though larger bone chariots are possible, especially when ostovites work together."
  - name: "Scuttle Away"
    desc: "`pf2:r` **Trigger** The ostovite's bone chariot is destroyed <br>  <br> **Effect** The ostovite within Steps or Strides."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +9 (`pf2:1`) (finesse, magical, unholy), **Damage** 1d4 piercing plus 1d4 acid"
  - name: "Melee strike"
    desc: "Bone Spike +9 (`pf2:1`) (finesse, unholy), **Damage** 1d12 piercing plus 1d4 bleed"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Skittering scavenger vermin common throughout the Abyss, ostovites roam battlefields to harvest flesh and bones. After the ostovites dissolve and slurp up the flesh for sustenance, they craft the bones into elaborate shells they refer to as "bone chariots."

These bone chariots move under the ostovites' command and serve as an important marker of rank in ostovite nests. To the tiny ostovites, bigger is better, and building large skeletal conveyances is the only way for them to increase their standing in life. Although they feel deeply inferior to creatures larger than themselves, this fear can be overwhelmed by the ostovites' visceral desire to harvest those creatures' bones to increase their own status. When confronted with a particularly massive skeleton, ostovites generally fight among themselves and end up splitting the haul. However, there are rare instances of the selfish creatures working together to puppeteer a much larger bone chariot.

Ostovites' faint understanding of anatomy results in bone chariots that look more like a nightmarish attempt at art than any creature the bones were pulled from. Some powerful fiends and their admirers collect this strange art by bribing ostovites with skeletons or finding ways to kill ostovites without disrupting the chariot around them.

Despite ostovites' origins in the Outer Rifts, they are neither demons nor qlippoth. Without the protection of the major fiends, they find their homes in nooks and crannies along the corners of their home plane. Though they have no innate ability to cross the planar boundaries, flaws in the Outer Rifts' fabric often lead them to worlds across the planes. Ostovites that have thus migrated are often much happier. Away from demonic abuse, they usually can be found near mortal crypts and battlefields. In the Universe, they rarely have to face any threats other than the undead, clerics of Pharasma, and families of the deceased.

```statblock
creature: "Ostovite"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
