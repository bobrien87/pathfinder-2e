---
type: affliction
sub-type: "{sub-type}"
source-type: "{source-type}"
traits: "{traits}"
saving-throw: "{saving-throw}"
onset: "{onset}"
max-duration: "{max-duration}"
source: "{source}"
---
### `= this.file.name`
**`= choice(this.sub-type != null, this.sub-type, "Affliction")`**
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= choice(this.saving-throw != null, "**Saving Throw** " + this.saving-throw, "") + choice(this.onset != null, choice(this.saving-throw != null, "; ", "") + "**Onset** " + this.onset, "") + choice(this.max-duration != null, choice(this.saving-throw != null or this.onset != null, "; ", "") + "**Max Duration** " + this.max-duration, "")`

***

{description}

#### Stages
- **Stage 1** {stage-1}
- **Stage 2** {stage-2}
- **Stage 3** {stage-3}

**Source:** `= this.source` (`= this.source-type`)
