---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Shove]]"]
price: "{'gp': 650}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple wooden *+1 striking mace* transforms in the hands of a wielder with great faith in a deity.

**Activate—Bow to a Higher Power** `pf2:1` (concentrate)

**Requirements** You worship a deity

**Effect** You supplicate yourself to your deity, and the *chaplain's cudgel* becomes a conduit for their power. It transforms into your deity's favored weapon, as the *[[Shifting]]* rune except that it functions even if the favored weapon is a ranged weapon, a weapon requiring two hands, or both. Etchings of your deity's religious symbol and other divine depictions spread across the weapon from end to end. This lasts until this activation is used again. While the weapon is attuned to you in this way, you get the following benefits.

- If you have the holy or unholy trait, you can add that trait to Strikes you make with the weapon.
- Whenever you cast a divine spell that takes 2 actions or more to cast, the next Strike you make with this weapon before the end of your next turn gets a status bonus to its damage roll equal to the weapon's number of damage dice. Casting a spell matching the options from your deity's divine font grants this benefit no matter how many actions you spent casting it.

**Source:** `= this.source` (`= this.source-type`)
