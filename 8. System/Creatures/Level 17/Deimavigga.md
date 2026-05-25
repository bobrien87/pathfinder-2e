---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deimavigga"
level: "17"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Greater Darkvision]]"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean (indominable oration, telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +29, Deception +34, Diplomacy +36, Intimidation +30, Religion +30, Society +27, Stealth +33"
abilityMods: ["+7", "+8", "+6", "+4", "+7", "+9"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "+4 Bonus on Perception to Sense motive"
    desc: ""
  - name: "Indomitable Oration"
    desc: "Any creature capable of comprehending speech understands the deimavigga, as if they constantly spoke in all languages at once."
  - name: "Boundless Reach"
    desc: "A deimavigga's razor-sharp claws can slice through reality, allowing them to make claw Strikes and use spells with a range of touch against any creature they can see directly or via magic. A creature targeted in this way can retaliate until the start of the deimavigga's next turn; it can target the devil's claws as if the devil were physically present and adjacent to the target, though the claws are [[Concealed]]."
armorclass:
  - name: AC
    desc: "40; **Fort** +27, **Ref** +29, **Will** +32"
health:
  - name: HP
    desc: "285; **Immunities** fire; **Weaknesses** holy 15; **Resistances** physical 15 except silver"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Whispers of Discord"
    desc: "`pf2:r` **Trigger** A creature within 60 feet is targeted by a spell that would restore Hit Points or provide a status bonus (the deimavigga automatically recognizes such effects) <br>  <br> **Effect** The deimavigga whispers disturbing lies, audible only to the target, to shake the target's faith in the spell's caster. The target must attempt a DC 38 [[Will]] save. <br> - **Critical Success** The target disbelieves the lies and receives the intended benefit of the spell; the target becomes temporarily immune to Whispers of Discord for 24 hours. <br> - **Success** As critical success, but the target isn't temporarily immune. <br> - **Failure** The spell fails to affect the target. The target refuses all aid from that caster for 1 round and doesn't count as the caster's ally. <br> - **Critical Failure** As failure, but the duration is 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, finesse, magical, unarmed, unholy), **Damage** 3d8+18 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +34<br>**7th** [[Divine Decree]], [[Warp Mind]]<br>**6th** [[Dominate]], [[Scrying]]<br>**5th** [[Illusory Scene]]<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**3rd** [[Dream Message]] (At Will)<br>**2nd** [[Stupefy]] (At Will)<br>**1st** [[Illusory Disguise]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The deimavigga can take on the appearance of any humanoid. This doesn't change their Speed or attack and damage bonuses with Strikes but might change the damage type their Strikes deal (typically to bludgeoning). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Whisper Earworm"
    desc: "`pf2:1` The deimavigga whispers a terrifying multiversal truth to one adjacent creature, shaking its faith in reality and divinity. The target must attempt a DC 38 [[Will]] save. Celestials and fiends gain a +2 status bonus to this save. <br> - **Critical Success** The target is unaffected and temporarily immune to Whisper Earworm for 24 hours. <br> - **Success** The target is unaffected. <br> - **Failure** The next time the target rests, it ruminates on the deimavigga's words instead of sleeping or otherwise resting and awakens [[Fatigued]]. The target also becomes [[Drained]] 1 and [[Stupefied 1]] until it's no longer fatigued. <br> - **Critical Failure** As failure, but [[Drained]] 2. After this rest, the target must attempt another DC 38 [[Will]] save. On a failure, the target becomes [[Stupefied 2]] and takes a –4 status penalty to Will saves against effects from unholy creatures. These effects last until the target unlearns the truth spoken by the deimavigga, requiring a [[Rewrite Memory]] spell, other means of modifying their memory, or powerful magic such as a [[Wish]] ritual. <br>  <br> > [!danger] Effect: Whisper Earworm (Critical Failure)"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

As masters of cold, calculated logic and perfectly timed proselytization, the loathsome deimaviggas seek to set friend against friend and turn the faithful from their beliefs at every opportunity. Their most common tools are mortal ego and despair. Those who are high-ranking or ambitious among their faith are lured toward self-aggrandizement until they see themselves first and their deity and clergy second. Those prone to doubt or heartache are isolated, as the deimavigga disrupts their divine spells and weakens their faith.

There are countless legions of lawful fiends in the nine layers of Hell, warring against the celestial planes and scouring the Material Plane for souls to corrupt.

```statblock
creature: "Deimavigga"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
