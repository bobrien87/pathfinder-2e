---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Scrying]]"]
price: "{'gp': 125}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A watchful portrait appears to be an innocuous depiction of a bored noble, unassuming relative, or unknown local celebrity. You Activate the portrait by hanging it. While it's activated, you can use a single action with the concentrate trait to see through the eyes of the portrait instead of your own. You can do so while you're within 500 feet of the portrait, even if it's outside your line of sight or line of effect. You visually observe the area around the portrait from its perspective, using your own visual senses. While you're scrying through it, the portrait's eyes follow others more than usual. A creature that succeeds at a DC 30 [[Perception]] check notices this phenomenon.

The scrying ends after 10 minutes or when you decide to stop watching through the portrait. The painting loses its magic when the scrying ends, if 4 hours pass after you Activate it without you looking through it, or if you Activate a different watchful portrait. The portrait then remains a normal, non-magical work of art, but due to its rather bland subject matter, it is worth no more than 5 gp.

**Source:** `= this.source` (`= this.source-type`)
