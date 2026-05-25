---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Courtesan"
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
    desc: "+9"
languages: "Common (plus two additional languages)"
skills:
  - name: Skills
    desc: "Deception +12, Diplomacy +12, Performance +13, Society +10, Art Lore +12"
abilityMods: ["-1", "+3", "+0", "+2", "+3", "+4"]
abilities_top:
  - name: "+4 to Sense Motive"
    desc: ""
  - name: "Group Impression"
    desc: "When the courtesan [[Makes an Impression]], they can compare their Diplomacy check result to the Will DCs of up to four targets instead of one."
  - name: "Social Specialist"
    desc: "When entertaining or socializing, the courtesan is a 5th-level challenge."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +7, **Will** +11"
health:
  - name: HP
    desc: "25"
abilities_mid:
  - name: "Beguiling Presence"
    desc: "10 feet. <br>  <br> Creatures in the area that can observe the courtesan take a –2 status penalty on their Will DC against the courtesan's attempts to make a `act request` of them."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sword Cane +9 (`pf2:1`) (agile, concealable, finesse), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Cutting Remarks"
    desc: "`pf2:1` The courtesan levies insults or backhanded compliments, attempting to `act demoralize skill=performance` a creature using their Performance modifier instead of Intimidation."
  - name: "Words of Encouragement"
    desc: "`pf2:1` The courtesan praises the performance of one ally who can hear them. The targeted ally ignores any circumstance and status penalties they have until the start of the courtesan's next turn. The target then becomes temporarily immune to this ability for 10 minutes. <br>  <br> > [!danger] Effect: Words of Encouragement"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Courtesans are high-class entertainers and professional companions, paid in favors and privileges for the honor of their company. These trendsetting socialites levy their clout to consort with those above their station, maneuvering connections to build exclusive clientele and climb the social ladder. A courtesan's discretion and mobility among the different ranks of society make their friendship well worth the price.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Courtesan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
