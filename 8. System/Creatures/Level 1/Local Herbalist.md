---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Local Herbalist"
level: "1"
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
    desc: "+7"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +6, Diplomacy +4, Nature +7, Survival +7"
abilityMods: ["+3", "+0", "+1", "+1", "+4", "+0"]
abilities_top:
  - name: "Herbalism Specialist"
    desc: "For encounters involving collecting herbs or making medicine from them, the local herbalist is a 3rd-level challenge."
  - name: "Natural Medicine"
    desc: "The herbalist can use Nature instead of Medicine to [[Treat Wounds]] or [[Administer First Aid]], and gains a +3 circumstance bonus to the check if they're in the wilderness with access to fresh herbal ingredients."
armorclass:
  - name: AC
    desc: "13; **Fort** +8, **Ref** +5, **Will** +9"
health:
  - name: HP
    desc: "24"
abilities_mid:
  - name: "Saving Touch"
    desc: "`pf2:r` **Frequency** once per 10 minutes <br>  <br> **Trigger** An ally close enough for the herbalist to reach with a Stride is reduced to 0 Hit Points <br>  <br> **Effect** The herbalist Strides until adjacent to the ally and [[Administers First Aid]] to that ally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +5 (`pf2:1`) (two hand d8), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Ranged strike"
    desc: "Fungal Spores +7 (`pf2:1`) (fungus, poison, range 10 ft.), **Damage** 1d4 poison plus 1d4 poison"
spellcasting: []
abilities_bot:
  - name: "Prompt Poultice"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The local herbalist quickly mixes together a potent healing salve with the most precious ingredients from their medicine bag. They create a temporary lesser elixir of life. This elixir remains potent for 1 round before becoming sour and useless."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Local herbalists use their understanding of the natural world to heal and restore balance. Most join a secret lodge that teaches these ancient arts.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Local Herbalist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
