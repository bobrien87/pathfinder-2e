---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Intelligent]]", "[[Occult]]", "[[Shove]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Perception +11; precise vision 30 feet, imprecise hearing 30 feet

Communication telepathy (Common, Varisian)

Skills Survival +28, Warfare Lore +35

Int +6, Wis +3, Cha +3

Will +28

It's uncertain how or why the intelligence occupying this *+2 greater striking shifting warhammer* came to be there, but over its many years of battlefield experience, it has proven itself to be a brilliant military tactician on par with some of history's greatest generals. Its earliest appearance was in the hands of its namesake, General Lord Draddeth, who attributed many of his successful campaigns to the counsel of a magical hammer he had commissioned during the Molthuni Cessation from Cheliax. Though the hammer disappeared upon the general's death, its legend has persisted, and the colloquialism "the Draddeth Edge"—referring to a natural talent for strategic planning and quick thinking—remains in common usage across Molthune.

*Draddeth's Edge* possesses a deep and abiding sense of patriotism for the nation of Molthune that sometimes outweighs its loyalty to those wielding it. Wielders who consistently express disrespect for Molthune or admiration for its enemies, or who fail to show proper respect for the hammer's tactical prowess, inevitably find it missing at some crucial moment when it departs in search of a more suitable comrade in arms. Conversely, it's unwaveringly loyal to and difficult to separate from those it deems worthy of its devotion. As long as you draw breath, the hammer can't be knocked from your grasp or dropped unless you will it, even remaining in your hand if you're rendered [[Unconscious]]. It also grants an item bonus equal to the bonus it gains from any currently affixed potency rune to recovery checks you make while dying.

**Source:** `= this.source` (`= this.source-type`)
