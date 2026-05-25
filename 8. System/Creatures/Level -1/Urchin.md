---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Urchin"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Deception +4, Society +3, Stealth +5, Survival +3, Thievery +7"
abilityMods: ["-1", "+3", "+0", "+1", "+1", "+2"]
abilities_top:
  - name: "Collaborative Thievery"
    desc: "The urchin gains a +1 circumstance bonus to [[Steal]] or [[Palm an Object]] while within 10 feet of an ally who has the pickpocket ability."
  - name: "Pickpocket"
    desc: "For an urchin, the DC to `act steal` or `act palm-an-object` isn't increased by 5 for an item that's closely guarded. They can Steal objects that would be extremely noticeable or time-consuming to remove (like worn shoes, armor, or actively wielded objects)."
armorclass:
  - name: AC
    desc: "15; **Fort** +2, **Ref** +7, **Will** +3"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shiv +5 (`pf2:1`) (agile), **Damage** 1d4-1 piercing"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4-1 bludgeoning"
  - name: "Melee strike"
    desc: "Rock +5 (`pf2:1`) (thrown 10), **Damage** 1d4-1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Although their escapades might be notorious, few urchins are thrill-seekers. For some urchins, when begging alone is not enough to fill their bellies, theft becomes a viable survival tactic. Many underworld powers also use urchins as spies and messengers, while training them to become future pickpockets, burglars, and foot soldiers.

Unfortunately, every society has people living on its fringes. While good communities work to grant aid and respite to their downtrodden, sometimes-due to economic downturn, famine, or war-the ranks of the less fortunate exceed the community's capacity to support them. In heartless neutral and evil societies, poverty is seen as an inevitability that can never be truly eradicated, or even worse, as a tool to be manipulated for political gain.

```statblock
creature: "Urchin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
