---
type: creature
group: ["Humanoid", "Ratfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Swarm Voice"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Common, Ysoki"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Diplomacy +17, Intimidation +15, Performance +15, Society +16, Survival +10, Legal Lore +16"
abilityMods: ["+2", "+1", "+0", "+3", "+3", "+4"]
abilities_top:
  - name: "+9 to Sense Motive"
    desc: ""
  - name: "Voice of the Swarm"
    desc: "For encounters involving negotiation or diplomacy, the swarm voice is a 7th-level challenge."
  - name: "Swarming"
    desc: "A swarm voice can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +8, **Will** +11"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +11 (`pf2:1`) (reach), **Damage** 1d8+5 piercing"
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (agile, unarmed), **Damage** 1d4+5 piercing"
  - name: "Ranged strike"
    desc: "Alchemical Bomb +10 (`pf2:1`) (bomb, consumable, splash), **Damage** 1 acid plus 1d6 acid plus 1 acid"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Advise Swarm"
    desc: "`pf2:2` The swarm voice issues orders to move. Each ratfolk from the same warren in a @Template[type:emanation|distance:15] can spend a reaction to Step, Stride, or [[Take Cover]]."
  - name: "Chittering Terror"
    desc: "`pf2:2` The swarm voice chitters, creating a terrifying din, and encourages their allies to join in. Each enemy within @Template[emanation|distance:30]{30 feet} must succeed at a DC 19 [[Will]] save or be [[Frightened]] 1 (or [[Frightened]] 2 on a critical failure). An enemy takes a –2 circumstance penalty to its save if it's adjacent to one or more ratfolk allied with the swarm voice. Regardless of the result of a creature's save, it's then temporarily immune for 1 hour."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The swarm voice is the secular leader of a ysoki warren or one family in a larger warren. If there is a dispute, the swarm voice resolves it. If there is a negotiation, they orchestrate it. If war is about to break out, they declare it. The swarm voice is the welcoming hand and the iron fist of their colony.

Ysoki (or, as outsiders call them, ratfolk) in their warrens have a society that is both stern and democratic, caring and ever vigilant. And at the top is a handful of intimidating and protective figures who make sure the swarm remains safe.

```statblock
creature: "Swarm Voice"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
