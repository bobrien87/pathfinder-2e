---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Activating this vial of colorless liquid requires inserting a small amount of another chemical or material, such as blood or mud. The vial reacts rapidly, transforming into a murky, reddish-brown substance.

Once activated, the dye remains potent for up to 10 minutes, during which time you can spend 1 minute to brush it onto a single object of up to 1 Bulk or across the ground in a single 5-foot square. Where the dye comes in contact with an exact match for the activating chemical, it takes on a bright blue hue, while staying transparent in areas where there is no activating component present.

**Source:** `= this.source` (`= this.source-type`)
