package com.avnet.pours.entities;

import com.avnet.pours.entities.listeners.AuditListener;
import com.avnet.pours.entities.listeners.PostTransactListener;
import com.avnet.pours.entities.listeners.PreTransactListener;
import com.avnet.pours.entities.model.AuditableEntity;
import com.fasterxml.jackson.annotation.JsonFilter;

import javax.persistence.*;
import java.sql.Timestamp;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Objects;


@Entity
@Table(name ="pours_failed_receipt_scans")
@EntityListeners({ AuditListener.class, PreTransactListener.class, PostTransactListener.class })
@JsonFilter("auditFilter")
public class FailedReceiptScan extends AuditableEntity<com.avnet.pours.entities.FailedReceiptScan> {

    public FailedReceiptScan() { super(); }

    @Id
    @Column(name = "record_id")
    private String recordId;

    @Column(name="user_id")
    private String userId;

    @Column(name="company_id")
    private Integer companyId;

    @Column(name="failure_message")
    private String failureMessage;

    @Column(name="receipt_type")
    private String receiptType;

    @Column(name="part_number")
    private String partNumber;

    @Column(name="location")
    private String location;

    @Column(name ="site_code")
    private String siteCode;

    @Column(name="order_qty")
    private Integer orderQuantity;

    @Column(name="ref_number")
    private String refNumber;

    @Column(name="mfg")
    private String note;

    @Column(name="mfg_part")
    private String mfgPart;

    @Column(name="po")
    private String PO;

    @Column(name="rfo_num")
    private Long rfoNum;

    @Column(name="F1")
    private String f1;

    @Column(name="F2")
    private String f2;

    @Column(name="F3")
    private String f3;

    @Column(name="F4")
    private String f4;

    @Column(name="F5")
    private String f5;

    @Column(name="F6")
    private String f6;

    @Column(name="F7")
    private String f7;

    @Column(name="F8")
    private String f8;

    @Column(name="F9")
    private String f9;

    @Column(name="F10")
    private String f10;

  @Column(name="order_number")
  private Integer orderNumber;

    @Column(name="packing_slip_num")
  private String packingSlipNum;

  @Column(name="date_created")
  private Date dateCreated;

    public String getRecordId() {
        return recordId;
    }

    public void setRecordId(String recordId) {
        this.recordId = recordId;
    }

    public String getFailureMessage() {
        return failureMessage;
    }

    public void setFailureMessage(String failureMessage) {
        this.failureMessage = failureMessage;
    }

    public String getPartNumber() {
        return partNumber;
    }

    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public Integer getCompanyId() {
        return companyId;
    }

    public void setCompanyId(Integer companyId) {
        this.companyId = companyId;
    }

    public Integer getOrderQuantity() {
        return orderQuantity;
    }

    public void setOrderQuantity(Integer orderQuantity) {
        this.orderQuantity = orderQuantity;
    }

    public String getSiteCode() {
        return siteCode;
    }

    public void setSiteCode(String siteCode) {
        this.siteCode = siteCode;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public String getPO() {
        return PO;
    }

    public void setPO(String PO) {
        this.PO = PO;
    }

    public String getReceiptType() {
        return receiptType;
    }

    public void setReceiptType(String receiptType) {
        this.receiptType = receiptType;
    }

    public String getRefNumber() {
        return refNumber;
    }

    public void setRefNumber(String refNumber) {
        this.refNumber = refNumber;
    }

    public String getMfgPart() {
        return mfgPart;
    }

    public void setMfgPart(String mfgPart) {
        this.mfgPart = mfgPart;
    }

    public Integer getOrderNumber() {
        return orderNumber;
    }

    public void setOrderNumber(Integer orderNumber) {
        this.orderNumber = orderNumber;
    }

    public String getPackingSlipNum() {
        return packingSlipNum;
    }

    public void setPackingSlipNum(String packingSlipNum) {
        this.packingSlipNum = packingSlipNum;
    }

    public Date getDateCreated() {
        return dateCreated;
    }

    public void setDateCreated(Date dateCreated) {
        this.dateCreated = dateCreated;
    }



    public String getF1() {
        return f1;
    }

    public void setF1(String f1) {
        this.f1 = f1;
    }

    public String getF2() {
        return f2;
    }

    public void setF2(String f2) {
        this.f2 = f2;
    }

    public String getF3() {
        return f3;
    }

    public void setF3(String f3) {
        this.f3 = f3;
    }

    public String getF4() {
        return f4;
    }

    public void setF4(String f4) {
        this.f4 = f4;
    }

    public String getF5() {
        return f5;
    }

    public void setF5(String f5) {
        this.f5 = f5;
    }

    public String getF6() {
        return f6;
    }

    public void setF6(String f6) {
        this.f6 = f6;
    }

    public String getF7() {
        return f7;
    }

    public void setF7(String f7) {
        this.f7 = f7;
    }

    public String getF8() {
        return f8;
    }

    public void setF8(String f8) {
        this.f8 = f8;
    }

    public String getF9() {
        return f9;
    }

    public void setF9(String f9) {
        this.f9 = f9;
    }

    public String getF10() {
        return f10;
    }

    public void setF10(String f10) {
        this.f10 = f10;
    }

    public Long getRfoNum() {
        return rfoNum;
    }

    public void setRfoNum(Long rfoNum) {
        this.rfoNum = rfoNum;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        FailedReceiptScan receipt = (FailedReceiptScan) o;
        return Objects.equals(recordId, receipt.recordId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(recordId);
    }

}


