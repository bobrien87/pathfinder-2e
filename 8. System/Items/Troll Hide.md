---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Healing]]"]
price: "{'gp': 6000}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tissue from a living forest troll has been integrated through this hide armor. This armor has two organic receptacles on its back that can each hold a single Elixir of Life. One elixir takes 3 Interact actions to install. For the armor to function properly, each elixir must be the same level.

**Activate** `pf2:1` (manipulate)

**Requirements** Two elixirs of life are installed in the armor

**Effect** Regenerating tissue from the armor fills your wounds for 8 rounds. At the start of each of your turns, you regain Hit Points equal to the level of the loaded elixirs. Each time you regain at least 13 Hit Points from the armor, you regrow one damaged or ruined organ. During a round that you regain 9 or more Hit Points from the armor, you can reattach severed body parts by spending an Interact action to hold the body part to the area it was severed from. If you take electricity or fire damage, the armor deactivates until the end of your next turn. (Similar armor from other types of trolls might be deactivated by different damage types.) In the event the armor itself is damaged, it will restore its own Hit Points before it resumes healing you. The activation uses up the elixirs, and the armor can't be activated again until two new ones are installed.

**Source:** `= this.source` (`= this.source-type`)
