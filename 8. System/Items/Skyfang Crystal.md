---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *skyfang crystal* appears as a softly glowing length of blue crystal shaped like a gently curved fang; it's typically affixed to a short length of chain, allowing it to be worn as a necklace or wrapped around a forearm. The light it sheds is equal in strength to that of a candle; it can't be extinguished but can be blocked simply by wrapping the crystal in cloth, wearing it under clothing, or keeping it in a container. The first of these magical crystals was believed to have been created by a dying dragon who'd spent her life fighting against evil spirits. She plucked a dozen of her smallest teeth from her jaw and offered them to her 12 most trusted allies so that they could continue to track down evil spirits and remain protected as they did so, even after she was gone.

As long as you have a *skyfang crystal* invested, you gain mental resistance 10. If you're unholy, you're [[Enfeebled]] 2 while you have a *skyfang crystal* invested.

**Activate—[[Seek]] the Unholy** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You touch the *skyfang crystal* to your brow and utter the name of a specific fiend or spirit you seek. If the target is on the same plane as you, the *skyfang crystal* pulses stronger with light when you face in the approximate direction of the named creature, allowing you to [[Track]] that creature. The DC for this check is equal to the creature's Will DC, and you can use Occultism, Religion, or Survival to attempt the check. As long as you're tracking this fiend or spirit, you gain a +2 item bonus to saving throws against effects that creature generates. This effect persists until you activate the *skyfang crystal* again to track a different target.

> [!danger] Effect: Skyfang Crystal

**Source:** `= this.source` (`= this.source-type`)
