---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Forest Troll"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Troll"
trait_04: "Wood"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Jotun"
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +12"
abilityMods: ["+5", "+2", "+6", "-2", "+0", "-2"]
abilities_top:
  - name: "Easily Misled"
    desc: "The forest troll gets a –4 circumstance penalty to their Perception DC against Deception checks."
armorclass:
  - name: AC
    desc: "20; **Fort** +17, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "125; regeneration 20 (deactivated by electricity or fire); **Weaknesses** fire 10, electricity 10"
abilities_mid:
  - name: "Regeneration 20 (Deactivated by Electricity or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Furious Flailing"
    desc: "`pf2:r` **Trigger** The forest troll takes electricity or fire damage <br>  <br> **Effect** The troll makes a claw Strike against a random creature within its reach. If the troll has persistent fire damage, they attempt a DC 15 flat check to remove it."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+5 piercing"
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d8+5 slashing"
spellcasting: []
abilities_bot:
  - name: "Chase Prey"
    desc: "`pf2:2` The forest troll rushes forward on all fours, Striding and then making two claw Strikes."
  - name: "Rend"
    desc: "`pf2:1` Claw <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Forest trolls are gangly giants who stalk the fringes of civilization. They rely on their incredible strength to overpower foes with their vicious claws and toothy maws. These trolls stand anywhere from 12 to 16 feet tall, though they prefer to hunch for comfort and to lull foes into a false sense of security. Trolls are truly creatures of the forest, deeply linked in flesh and blood to the verdant habitats they consider their territory. In fact, when a forest troll is killed, their flesh turns into blackened lumps of charcoal, often still glowing with coals. Despite that, these creatures roam farther and wider than most of their kin, to the extent that they're the first creatures a common person thinks of when they hear the word "troll."

Slavering, cruel, invincible brutes: this is the villager's stock description for the dread monsters known as trolls. The roots of these stories are undoubtedly true. Trolls' flesh endlessly regrows, going so far as to sprout aberrant limbs or additional heads if not pruned, and a bottomless hunger is required to feed such unfettered growth. Even in the process of glutting themselves, however, trolls find opportunities to taunt their prey and inflict petty cruelties.

A troll's ability to survive is so strong that they believe even the smallest scrap of flesh will slowly regenerate into a new form, suffering as all the powers of the land are gathered to revive them. Despite the pain, trolls speak of this unassailable vitality as a blessing from their creator. Few trolls have heard the laughter of demons who claim that creator cursed the trolls and cast them down from lofty heights, binding them so they could never rise again.

Trolls prefer to remain solitary, keeping every scrap of food for themselves. In rare instances, an old and powerful troll comes to lead groups of trolls. Such warleaders possess enough cunning to lead their hordes in devastating raids and massacres, and their presence permanently alters the surrounding ecosystem. This link to their environment is an often misunderstood aspect of trollkind, and grows more acute with a troll's age and power. That's not to say trolls are valorous protectors of nature. They're vicious and territorial, and will blight their own territory forever if it means more to eat for a day.

```statblock
creature: "Forest Troll"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
