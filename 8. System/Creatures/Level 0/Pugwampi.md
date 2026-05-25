---
type: creature
group: ["Fey", "Gremlin"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pugwampi"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Kholo, Sakvroth"
skills:
  - name: Skills
    desc: "Crafting +2, Deception +2, Nature +4, Stealth +5, Thievery +5"
abilityMods: ["-3", "+3", "+0", "+0", "+2", "-2"]
abilities_top:
  - name: "-2 Penalty on Perception to Hear things"
    desc: ""
armorclass:
  - name: AC
    desc: "14; **Fort** +5, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "17; **Weaknesses** cold iron 2"
abilities_mid:
  - name: "Unluck Aura"
    desc: "20 feet. <br>  <br> When a creature that isn't an animal, gremlin, or kholo enters the aura, it might become unlucky. It attempts a DC 16 [[Will]] save; it must roll twice and take the worse result. On a success, the creature is temporarily immune to pugwampi unluck auras for 24 hours. On a failure, the creature must roll twice and take the worse result on all checks as long as it's within the aura. <br>  <br> > [!danger] Effect: Unluck Aura"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +8 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d6-3 slashing"
  - name: "Ranged strike"
    desc: "Shortbow +8 (`pf2:1`) (deadly d10, magical, reload 0, range 60 ft.), **Damage** 1d6 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 16, attack +8<br>**2nd** [[Speak with Animals]] (At Will)<br>**1st** [[Prestidigitation]]"
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Mean, dog-faced, and craven, pugwampis take disproportionate enjoyment from the accidents and missteps of other creatures—something that happens often due to the supernatural aura of ill fortune these gremlins project. They enjoy preparing pranks involving spikes, excrement, pits full of spiders, and similar twisted torments. Pugwampis are somewhat deaf and thus often yell loudly to each other when not hiding. Many pugwampis worship kholos as gods and aspire to be more like them. Kholos, on the other hand, hate pugwampis because of their sycophantic fawning.

Gremlins are cruel fey tricksters and saboteurs who have fully acclimated to life in the Universe, finding distinct niches for their inventive destructiveness. Nearly all gremlins delight in ruining or breaking things, whether it's something physical like a device or vehicle or something intangible such as an alliance or relationship. A gremlin's greatest joy is watching the collapse of complex creations, preferably after the slightest, carefully targeted nudge from the gremlin. Gremlins tend to denigrate, bully, or even slaughter their lesser kin, particularly mitflits, whom stronger gremlins derisively call "baggies."

```statblock
creature: "Pugwampi"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
