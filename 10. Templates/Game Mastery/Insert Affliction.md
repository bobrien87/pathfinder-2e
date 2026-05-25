---
type: affliction
sub-type: "{sub-type}"
source-type: "{source-type}"
traits:
saving-throw: "{saving-throw}"
onset: "{onset}"
max-duration: "{max-duration}"
source: "{source}"
---
### `= this.file.name`
**`= choice(this.sub-type != null and this.sub-type != "", this.sub-type, "Affliction")`**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`

`= choice(this.saving-throw != null and this.saving-throw != "", "**Saving Throw** " + this.saving-throw, "") + choice(this.onset != null and this.onset != "", choice(this.saving-throw != null and this.saving-throw != "", "; ", "") + "**Onset** " + this.onset, "") + choice(this.max-duration != null and this.max-duration != "", choice(this.saving-throw != null and this.saving-throw != "" or this.onset != null and this.onset != "", "; ", "") + "**Max Duration** " + this.max-duration, "")`

{description}

#### Stages
- **Stage 1** {stage-1}
- **Stage 2** {stage-2}
- **Stage 3** {stage-3}

**Source:** `= this.source` (`= this.source-type`)
