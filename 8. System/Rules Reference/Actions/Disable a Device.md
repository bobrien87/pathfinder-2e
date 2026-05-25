---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

This action allows you to disarm a trap or another complex device. Often, a device requires numerous successes before becoming disabled, depending on its construction and complexity. A [[Thieves' Toolkit]] is helpful and sometimes even required to Disable a Device, as determined by the GM, and sometimes a device requires a higher proficiency rank in Thievery to disable it.

Your Thievery check result determines your progress.
- **Critical Success** You disable the device, or you achieve two successes toward disabling a device requiring more than one success. You leave no trace of your tampering, and you can rearm the device later, if that type of device can be rearmed.
- **Success** You disable the device, or you achieve one success toward disabling a device that requires more than one success.
- **Critical Failure** You trigger the device.

**Source:** `= this.source` (`= this.source-type`)
