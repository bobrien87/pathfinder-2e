---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tonic Merchant"
level: "3"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Crafting +11, Diplomacy +9, Medicine +10, Society +9, Mercantile Lore +9"
abilityMods: ["+0", "+2", "+1", "+4", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "50"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Acid Flask (Moderate) +10 (`pf2:1`) (splash, thrown 30), **Damage** 2d6 acid plus 2 acid"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Healing Bomb"
    desc: "`pf2:2` The tonic merchant quickly crafts a [[Antidote (Lesser)]], [[Antiplague (Lesser)]], or [[Elixir of Life (Minor)]] and lobs it at a willing or [[Unconscious]] ally within 30 feet. The elixir affects the ally as though they imbibed it. <br>  <br> The tonic merchant can use the rarest materials in their toolkit to improve the item to a [[Antidote (Moderate)]], [[Antiplague (Moderate)]], or [[Elixir of Life (Lesser)]]. Afterward, they must spend 10 minutes gathering new ingredients before they can do so again."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

This alchemist sells healing potables, but might offer their services without a fee to those truly in need.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Tonic Merchant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
