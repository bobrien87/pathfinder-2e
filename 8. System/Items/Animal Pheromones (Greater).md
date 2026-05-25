---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Olfactory]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (Interact)

These chemicals convey myriad signals. Many varieties of these alchemical cocktails exist, each tailored for the unique chemistry of a specific type of animal. You can, for example, make wolf pheromones, but not pheromones that affect all animals. The pheromones don't work on creatures that are similar to the specific kind of animal, but aren't actually animals—for example, wolf pheromones don't work on werewolves. When you learn the formula for animal pheromones, you learn the formulas for all common animals. If no animals of a kind are common, you must learn the formula for it separately, and the formula has the same rarity as the least-rare creature of that kind.

You Activate animal pheromones by rubbing them on yourself or a creature within reach. The pheromones last for 24 hours or until scrubbed clean with 1 minute of work (consisting of multiple Interact actions). During this time, the pheromones exude a subtle aroma in a @Template[emanation|distance:15]{15-foot radius} that calms and influences the designated animals. A designated animal that ends its turn within the affected area must attempt a DC 35 [[Will]] save saving throw with the following effects. The animal is then temporarily immune to the pheromones for 24 hours. The effect lasts for the duration of the pheromones, even after the creature leaves the affected area.
- **Critical Success** The animal is unaffected. It doesn't necessarily become aware of the pheromones, although intelligent animals might become suspicious if they observe others of their kind being affected.
- **Success** The animal's attitude toward the affected creature improves by one step. If this improves its attitude to at least indifferent, it can't take hostile actions against the affected creature, though the change in attitude ends as soon as the affected creature takes a hostile action against the animal or its allies.
- **Failure** As success, but the attitude increases by two steps.
- **Critical Failure** As success, but the attitude increases to helpful.

**Source:** `= this.source` (`= this.source-type`)
