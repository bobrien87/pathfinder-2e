---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Manipulate]]", "[[Thaumaturge]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Requirements** You are holding your chalice implement.

You drink from the liquid that slowly collects in your chalice or administer it to an adjacent ally. The drinker chooses whether to take a small sip or to drain the contents.

- **Sip** A sip grants the drinker an amount of temporary Hit Points equal to your level (minimum 3) that last until the end of your next turn.

> [!danger] Effect: Drink from the Chalice

- **Drain** (healing, vitality) Drinking deep instead heals the drinker @Damage[(3*@actor.level)[healing,vitality]|traits:healing,vitality]{3 Hit Points for each level} you have. After the chalice is drained, it's left with only its slowly collecting dregs; the chalice can't be drained again, though it can still be sipped from. If 10 minutes pass without anyone drinking from the chalice, it refills itself and can be drained again. If the drinker has @Damage[(3*@actor.level)[healing,void]|traits:healing,void]{void healing}, it can still heal in this way, and the effect has the void trait instead of healing and vitality.

**Source:** `= this.source` (`= this.source-type`)
