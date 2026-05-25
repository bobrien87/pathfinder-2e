---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This mask's features shift between various non-human elements, with each version reveling in grotesque and monstrous variations. During the festivals in Dhuraxilis, these masks are worn by influential and rich humans (or human-appearing populations) to better blend in with the monstrous crowds as they join in the revelry. While wearing the mask, you gain a +1 item bonus to Deception checks.

**Activate—Monstrosity Meld** `pf2:1` (concentrate, polymorph)

**Frequency** once per day

**Effect** You take on the general appearance of a type of non-humanoid creature that you can see, with the transformation lasting for 8 hours. Activating this effect doesn't change your traits or statistics, nor does it grant any of the special abilities of the creature you're imitating. It does not change your size, so a Medium creature that assumes the shape of a manticore remains Medium sized. This effect uses the same rules as the Impersonate activity of Deception. Onlookers always assume you're the chosen type of creature unless they're actively Seeking. You gain a +4 item bonus to your Deception DC against such Perception checks and add your level even if untrained.

**Source:** `= this.source` (`= this.source-type`)
