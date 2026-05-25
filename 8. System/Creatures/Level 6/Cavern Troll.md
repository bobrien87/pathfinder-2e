---
type: creature
group: ["Earth", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cavern Troll"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Troll"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Jotun, Sakvroth"
skills:
  - name: Skills
    desc: "Athletics +16, Intimidation +14"
abilityMods: ["+6", "+2", "+6", "-2", "+2", "-2"]
abilities_top:
  - name: "Easily Misled"
    desc: "The caverrn troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
  - name: "Rock Tunneler"
    desc: "A cavern troll can burrow through solid stone at a Speed of 10 feet. They can leave a tunnel if they desire."
armorclass:
  - name: AC
    desc: "22; **Fort** +16, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "135; **Immunities** bleed; **Weaknesses** acid 10, sonic 10"
abilities_mid:
  - name: "Regeneration 20 (Deactivated by Acid or Sonic)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Furious Throw"
    desc: "`pf2:r` **Trigger** The cavern troll takes acid or sonic damage <br>  <br> **Effect** The troll uses Throw Rock targeting a random enemy within their first range increment. If the cavern troll has persistent acid damage, they attempt a DC 15 flat check to remove it."
  - name: "Sunlight Petrification"
    desc: "If exposed to direct sunlight, a cavern troll immediately becomes [[Slowed]] 1 and can't use reactions. The slowed value increases by 1 each time the cavern troll ends its turn in sunlight. If the cavern troll's actions are reduced to 0 in this way, they become [[Petrified]] until they spends at least 1 minute in darkness. Spells like [[Sunburst]] that create magical sunlight can't petrify a cavern troll, but the troll is slowed 1 for 1d4 rounds after being exposed to such an effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+8 piercing"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d6+8 slashing"
  - name: "Ranged strike"
    desc: "Rock +16 (`pf2:1`) (brutal, range 120 ft.), **Damage** 1d12+8 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Throw Rock"
    desc: "`pf2:1` The monster picks up a rock within reach or retrieves a stowed rock and throws it, making a ranged Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Insatiable scavengers, cavern trolls stalk the eternal gloom of the Darklands, consuming all in their path—even rocks and minerals. These rocky goliaths can tunnel through stone with their iron-sharp claws. Despite a debilitating vulnerability to sunlight that petrifies them on sustained contact, hungry cavern trolls are often drawn to the comparatively lush surface world. Even when petrified, the immobile trolls are often mistaken for boulders or other natural phenomenon, leaving them free to hunt once night falls again. As cavern trolls age, their flinty skin becomes studded with small crystals and stones of various composition. Paragons of their kind have toothy maws replete with large crystalline fangs.

Towering brutes with slavering jaws and razor-sharp claws, trolls are voracious predators. A connection to the land not only rebuilds their bodies but creates countless varieties of trolls, each a reflection of the terrain that they draw upon. Trolls who migrate into new areas slowly transform as each body part is regenerated, leading to aberrant growth as new flesh tangles with the old.

```statblock
creature: "Cavern Troll"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
