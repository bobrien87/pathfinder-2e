---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 22000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An array of semiprecious stones is set into the ornate silver and beaten copper cover of this thick and weighty tome. If you open the book before it's been activated, its vellum pages are blank and pristine, but once activated, words dance and swim onto the pages before your eyes.

**Activate—Skim** 10 minutes (concentrate, manipulate)

**Effect** As you flip through the book, you think about a broad topic you want to know more about.

Choose one skill: Arcana, Crafting, Medicine, Nature, Occultism, Religion, Society, or a single subcategory of Lore. The book's pages fill with information about that skill, though only you can see the information.

While the pages are full, you can spend an Interact action perusing the book just before attempting a check to Recall Knowledge with the chosen skill. This grants you a +3 item bonus to the check, and if you roll a critical failure, you get a failure instead.

The information within the book disappears after 24 hours or when the tome is activated again.

**Source:** `= this.source` (`= this.source-type`)
