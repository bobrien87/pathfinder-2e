---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Guildmaster"
level: "8"
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
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Crafting +25, Diplomacy +24, Intimidation +22, Society +21, Architecture Lore +25, Bureaucracy Lore +19"
abilityMods: ["+3", "+1", "+2", "+4", "+2", "+3"]
abilities_top:
  - name: "Craft Specialist"
    desc: "For encounters involving matters of crafting or architecture, the guildmaster is a 12th-level challenge."
  - name: "Sworn Duty"
    desc: "While within the guild or presiding over guild business, the guildmaster gains a +2 circumstance bonus to weapon attack rolls and deals an additional 2d6 damage on a successful weapon attack."
armorclass:
  - name: AC
    desc: "26; **Fort** +14, **Ref** +14, **Will** +17"
health:
  - name: HP
    desc: "135"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Hammer +16 (`pf2:1`) (agile, magical), **Damage** 2d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Light Hammer +14 (`pf2:1`) (agile, magical, thrown 20), **Damage** 2d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Call to Action"
    desc: "`pf2:1` The guildmaster gives a speech to inspire themself and all guild-member allies within 60 feet, granting them a +1 status bonus to attack and damage rolls until the start of the guildmaster's next turn. <br>  <br> > [!danger] Effect: Call to Action"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

In cities, artisans working in a common trade often form guilds to set standards of quality, establish common prices, engage in collective bargaining with business owners, and lobby local governments for favorable laws. The guildmaster—often a master artisan in their own right—also acts as an administrator and politician, advocating for artisans in their trade.

Expertise is forged through years of effort and often tedious work. Artisans are masters of their craft, able to create works both practical and beautiful.

```statblock
creature: "Guildmaster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
