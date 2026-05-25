---
type: action
source-type: "Remaster"
traits: ["[[Inventor]]", "[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

Temporarily cranking the gizmos on your body into overdrive, you try to add greater power to your attacks. Attempt a [[Crafting]] check that has a standard DC for your level.

> [!danger] Effect: Overdrive
- **Critical Success** Your gizmos go into a state of incredible efficiency called critical overdrive, adding great power to your attacks. Your Strikes deal additional damage equal to your Intelligence modifier for 1 minute. After the Overdrive ends, your gizmos become unusable as they cool down or reset, and you can't use Overdrive for 1 minute.
- **Success** Your gizmos go into overdrive, adding power to your attacks. As critical success, except the additional damage is equal to half your Intelligence modifier.
- **Failure** Your gizmos whine concerningly and begin to smoke. Your Strikes deal 1 additional fire damage for 1 minute.
- **Critical Failure** Whoops! Something explodes. You take fire damage equal to half your level (rounded up), and you can't use Overdrive again for `r 1d4 #Recharge Overdrive` rounds as your gizmos reset.

**Special** When under the effects of Overdrive, you can still use the Overdrive action. You can't extend your Overdrive's duration this way, but you can turn an overdrive into a critical overdrive if you critically succeed. A failure has no effect on your current Overdrive, and you end your Overdrive on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
