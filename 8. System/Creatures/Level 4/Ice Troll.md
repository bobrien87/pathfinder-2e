---
type: creature
group: ["Cold", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ice Troll"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Troll"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Jotun"
skills:
  - name: Skills
    desc: "Athletics +10, Intimidation +10, Survival +10"
abilityMods: ["+5", "+2", "+5", "-2", "+2", "-2"]
abilities_top:
  - name: "Easily Misled"
    desc: "The ice troll takes a –4 circumstance penalty to their Perception DC against Deception checks."
  - name: "Ice Passage"
    desc: "An ice troll isn't impeded by difficult terrain caused by snow or ice, nor do they need to attempt Acrobatics checks to keep from falling on slippery ice."
armorclass:
  - name: AC
    desc: "19; **Fort** +13, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "90; **Immunities** cold; **Weaknesses** fire 10, sonic 10"
abilities_mid:
  - name: "Regeneration 15 (Deactivated by Fire or Sonic)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Furious Carve"
    desc: "`pf2:r` **Trigger** The ice troll takes fire or sonic damage <br>  <br> **Effect** The troll makes a hatchet or claw Strike against a random creature within reach. If the ice troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +13 (`pf2:1`) (agile, reach 10 ft., sweep), **Damage** 2d6+5 slashing"
  - name: "Melee strike"
    desc: "Hatchet +10 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 2d6+5 slashing"
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`) (reach 10 ft.), **Damage** 2d8+5 piercing"
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (agile, reach 10 ft.), **Damage** 2d4+5 slashing"
spellcasting: []
abilities_bot:
  - name: "Brutal Sweep"
    desc: "`pf2:3` **Requirements** The ice troll is wielding a hatchet <br>  <br> **Effect** The troll sweeps their hatchet in a large arc, dealing @Damage[3d6[slashing]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:5] (DC 18 [[Reflex]] save)."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ice trolls are nightmarish frozen monsters of rime-stained claws and hoarfrost teeth who haunt glaciers, mountains, and tundras. Their unceasing hunger drives them to pursue elk herds, seal colonies, and human villages. Ones that regenerate while sealed within ice floes or permafrost can be birthed from the ice during a thaw after being trapped for months, years, or even decades of unceasing hunger before they can finally break free.

Towering brutes with slavering jaws and razor-sharp claws, trolls are voracious predators. A connection to the land not only rebuilds their bodies but creates countless varieties of trolls, each a reflection of the terrain that they draw upon. Trolls who migrate into new areas slowly transform as each body part is regenerated, leading to aberrant growth as new flesh tangles with the old.

```statblock
creature: "Ice Troll"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
