---
type: creature
group: ["Construct", "Wyrwood"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wyrwood Sneak"
level: "1"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: "Wyrwood"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Common (Plus one regional language)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +5, Deception +7, Society +5, Stealth +7"
abilityMods: ["+0", "+4", "+0", "+2", "+1", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The wyrwood deals an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "16; **Fort** +3, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Living Machine"
    desc: "Though their body is an organic construct, a wyrwood is a living creature. They're not immediately destroyed when reduced to 0 HP, but rather fall [[Unconscious]] and eventually die. They don't need to eat or drink. They can be targeted by effects that target living creatures or that target constructs."
  - name: "No Breath"
    desc: "A wyrwood doesn't breathe and is immune to effects that require breathing (such as an inhaled poison)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Wyrwood sneaks specialize in moving unseen behind enemy lines, performing reconnaissance and quietly eliminating threats.

Originally created as sapient magical servants, wyrwoods reclaimed the means to make more of their kind from their oppressive originators; now, they fiercely defend their freedom and autonomy. These small, nimble living machines rely on their wits and speed to evade foes and gather information. Most wyrwoods are precise and calculating, to the point that many outsiders perceive them as unfeeling, but they're also highly curious and passionate about matters that pique their interest. Regardless of personal agenda, wyrwoods prioritize the survival of their people above all else, even to the detriment of others when necessary.

Despite gaining their freedom, wyrwoods struggle to establish a home in Avistan. Some people still view wyrwoods as tools of a secretive conspiracy, while others consider them traitorous servants who turned on their creators. Fearing for their safety, many wyrwoods fled the Inner Sea region to create a new home in Arcadia. The continent's eastern coast, known as the Grinding Coast, is home to large wyrwood populations. In the coastal city of Segada, wyrwoods live in relative peace and safety, but they still prefer insular lifestyles. Various wyrwood groups are scattered along the kingdoms of the Isles of the Empty Court off the Arcadian coast. The wyrwoods of these kingdoms sometimes serve as magical advisors, as understanding of aeon stones and other magical relics is common among wyrwood cultures.

Given their extreme self-reliance, wyrwoods have learned a degree of adaptability that far surpasses that of other cultures. When a wyrwood community finds itself in need of a specific skill or function, a member of the community—either a volunteer or one selected communally—takes it upon themself to learn the required abilities. They don't view any task as lesser or demeaning, as hubris is foreign to a wyrwood's construct nature.

A wyrwood's soul is tied to the magical stone that serves as their heart, which sometimes survives even when their construct body perishes. Another wyrwood might take the surviving heart from a close companion and incorporate it into their own body. In some cases, multiple wyrwoods might live on in a single body.

```statblock
creature: "Wyrwood Sneak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
